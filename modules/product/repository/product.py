from typing import List,Any,Dict
from modules.model.db import Products
from flask import current_app

class ProductRespository:
    def __init__(self,db):
        self.db = db 
        current_app.logger.info('ProductRepository instance created')

    def insert(self,prod:Products)->bool:
        try:
            self.db.session.add(prod)
            self.db.session.commit()
            current_app.logger.info('ProductRepository inserted record')
            return True
        except Exception as e:
            current_app.logger.info(f'ProductRepository insert error : {e}')
        return False
    
    def update(self,id:int,details:Dict[str,Any])->bool:
        try:
            self.db.session.query(Products).filter(Products.id==id).update(details)
            self.db.session.commit()
            current_app.logger.info('ProductRepository updated record')
            return True
        except Exception as e:
            current_app.logger.info(f'ProductRepository update error: {e}')
        return False
    
    def delete(self,id:int)->bool:
        try:
            self.db.session.query(Products).filter(Products.id==id).delete()
            self.db.session.commit()
            current_app.logger.info('ProductRepository deleted record')
            return True
        except Exception as e:
            current_app.logger.info(f'ProductRepository delete error: {e}')
        return False
    
    def select_all(self)->List[Any]:
        prds = self.db.session.query(Products).all()
        current_app.logger.info('ProductRepository full retrieval')
        return prds
    
    def select_one(self,id:int)->Any:
        prd = self.db.session.query(Products).filter(Products.id==id).one_or_none()
        current_app.logger.info('ProductRepository retrive by id')
        return prd 
    
    def select_one_code(self,code:str)->Any:
        prd = self.db.session.query(Products).filter(Products.code==code).one_or_none()
        current_app.logger.info('ProductRepository retrive by product code')
        return prd