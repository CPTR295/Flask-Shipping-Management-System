from typing import List,Any,Dict
from modules.model.db import Customer
from flask import current_app 

class CustomerRepository:
    def __init__(self,db):
        self.db = db 
        current_app.logger.info('CustomerRepository instance created')
    
    def insert(self,customer:Customer)->bool : 
        try:
            self.db.session.add(customer)
            self.db.session.commit()
            current_app.logger.info('CustomerRepository inserted record')
            return True
        except Exception as e:
            current_app.logger.info(f'CustomerRepository insert error : {e}')
        return False

    def update(self,id:int,details:Dict[str,Any]) -> bool:
        try:
            self.db.session.query(Customer).filter(Customer.id==id).update(details)
            self.db.session.commit()
            current_app.logger.info('CustomerRepository record updated')
            return True
        except Exception as e:
            current_app.logger.info(f'CustomerRepository update error : {e}')
        return False 

    def delete(self,id:int) ->bool:
        try:
            self.db.session.query(Customer).filter(Customer.id==id).delete()
            self.db.session.commit()
            current_app.logger.info('CustomerRepository record deleted')
            return True
        except Exception as e:
            current_app.logger.info(f'CustomerRepository delete error : {e}')
        return False 

    def select_one(self,id:int)->Any:
        cus = self.db.session.query(Customer).filter(Customer.id==id).one_or_none()
        self.db.session.commit()
        current_app.logger.info('CustomerRepository record retrival')
        return cus
    
    def select_all(self)->List[Any]:
        cus = self.db.session.query(Customer).all()
        self.db.session.commit()
        current_app.logger.info('CustomerRepository record full retrival')
        return cus
