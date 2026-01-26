from typing import Dict,Any,List
from modules.model.db import Payment,PaymentType
from flask import current_app

class PaymentRepository:
    def __init__(self,db):
        self.db = db 
        current_app.logger.info('PaymentRepository instance created')
    
    def insert(self,payment:Payment)->bool :
        try:
            self.db.session.add(payment)
            self.db.session.commit()
            current_app.logger.info('PaymentRepository inserted record')
            return True
        except Exception as e:
            current_app.logger.info(f'PaymentRepository insert error :{e}')
        return False
    
    def update(self,id:int,details:dict[str,Any])->bool:
        try:
            self.db.session.query(Payment).filter(Payment.id==id).update(details)
            self.db.session.commit()
            current_app.logger.info('PaymentRepository updated record')
            return True
        except Exception as e:
            current_app.logger.info(f'PaymentRepository update error : {e}')
        return False
    
    def delete(self,id:int)->bool:
        try:
            self.db.session.query(Payment).filter(Payment.id==id).delete()
            self.db.session.commit()
            current_app.logger.info('PaymentRepository deleted record')
            return True
        except Exception as e:
            current_app.logger.info(f'PaymentRepository delete error: {e}')
        return False
    
    def select_one(self,id:int)->Any :
        pay = self.db.session.query(Payment).filter(Payment.id==id).one_or_none()
        current_app.logger.info('PaymentRepository retrieve one by id')
        return pay
    
    def select_all(self,id:int)->List[Any] :
        pay = self.db.session.query(Payment).filter(Payment.id==id).all()
        current_app.logger.info('PaymentRepository retrieve all')
        return pay
    
    def select_one_reference(self,ref_no:str)->Any :
        pay = self.db.session.query(Payment).filter(Payment.ref_no==ref_no).one_or_none()
        current_app.logger.info('PaymentRepository retrieve one by ref_no')
        return pay
    
class PaymentTypeRepository:
    def __init__(self,db):
        self.db = db 
        current_app.logger.info('PaymentType Repository instance created')

    def insert(self,payt:PaymentType)->bool:
        try:
            self.db.session.add(payt)
            self.db.session.commit()
            current_app.logger.info('PaymentTypeRepository inserted record')
            return True
        except Exception as e:
            current_app.logger.info(f'PaymentTypeRepository insert error :{e}')
        return False
    
    def update(self,id:int,details:dict[str,Any])->bool:
        try:
            self.db.session.query(PaymentType).filter(PaymentType.id==id).update(details)
            self.db.session.commit()
            current_app.logger.info('PaymentTypeRepository updated record')
            return True
        except Exception as e:
            current_app.logger.info(f'PaymentTypeRepository update error : {e}')
        return False
    
    def delete(self,id:int)->bool:
        try:
            self.db.session.query(PaymentType).filter(PaymentType.id==id).delete()
            self.db.session.commit()
            current_app.logger.info('PaymentTypeRepository deleted record')
            return True
        except Exception as e:
            current_app.logger.info(f'PaymentTypeRepository delete error: {e}')
        return False
    
    def select_one(self,id:int)->Any :
        pay = self.db.session.query(PaymentType).filter(PaymentType.id==id).one_or_none()
        current_app.logger.info('PaymentTypeRepository retrieve one by id')
        return pay
    
    def select_all(self,id:int)->List[Any] :
        pay = self.db.session.query(PaymentType).filter(PaymentType.id==id).all()
        current_app.logger.info('PaymentTypeRepository retrieve all')
        return pay