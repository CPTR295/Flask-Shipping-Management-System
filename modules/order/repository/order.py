from typing import List,Any,Dict
from modules.model.db import Orders
from flask import current_app

class OrderRepository:
    def __init__(self,db):
        self.db = db 
        current_app.logger.info('OrderRespository instance created')

    def insert(self,order:Orders)->bool:
        try:
            self.db.session.add(order)
            self.db.session.commit()
            current_app.logger.info('OrderRepository inserted record')
            return True
        except Exception as e:
            current_app.logger.info(f'OrderRepository insert error:{e}')
        return False
        
    def update(self,id:int,details:Dict[str,Any])->bool:
        try:
            self.db.session.query(Orders).filter(Orders.id == id).update(details)
            self.db.session.commit()
            current_app.logger.info('OrderRepository updated record')
            return True
        except Exception as e:
            current_app.logger.info(f'OrderRepository update error : {e}')
        return False

    def delete(self,id:int)->bool:
        try:
            self.db.session.query(Orders).filter(Orders.id==id).delete()
            self.db.session.commit()
            current_app.logger.info('OrderRepository deleted record')
            return True
        except Exception as e:
            current_app.logger.info(f'OrderRepository delete error {e}')
        return False
    
    def select_all(self)->List[Any]:
        ords = self.db.session.query(Orders).all()
        current_app.logger.info('OrderRepository full retrieval')
        return ords 
    
    def select_one(self,id:int)->Any:
        ord = self.db.session.query(Orders).filter(Orders.id == id).one_or_none()
        current_app.logger.info('OrderRepository retrieval by id')
        return ord 
    
    def select_one_order(self,orderno:str)->Any:
        ord = self.db.session.query(Orders).filter(Orders.order_no==orderno).one_or_none()
        current_app.logger.info('OrderRepository retrieval by ordre number')
        return ord
