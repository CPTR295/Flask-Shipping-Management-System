from typing import List,Any,Dict
from modules.model.db import DeliveryOfficer
from flask import current_app

class DeliveryOfficerRepository:
    def __init__(self,db):
        self.db = db
        current_app.logger.info('DeliveryOfficerRepository instance created')

    def insert(self,officer:DeliveryOfficer)->bool:
        try:
            self.db.session.add(officer)
            self.db.session.commit()
            current_app.logger.info('DeliveryOfficerRepository record created')
            return True
        except Exception as e:
            current_app.logger.info(f'DeliveryOfficerRepository insert error {e}')
        return False
    
    def update(self,id:int,details:Dict[str,Any])->bool:
        try:
            self.db.session.query(DeliveryOfficer).filter(DeliveryOfficer.id==id).update(details)
            self.db.session.commit()
            current_app.logger.info('DeliveryOfficerRepository record updated')
            return True
        except Exception as e:
            current_app.logger.info(f'DeliveryOfficerRepository update error {e}')
        return False
    
    def delete(self,id:int)->bool:
        try:
            self.db.session.query(DeliveryOfficer).filter(DeliveryOfficer.id==id).detele()
            self.db.session.commit()
            current_app.logger.info('DeliveryOfficerRepository record delete')
            return True
        except Exception as e:
            current_app.logger.info(f'DeliveryOfficerRepository delete error {e}')
        return False
    
    def select_all(self)->List[Any]:
        dos = self.db.session.query(DeliveryOfficer).all()
        current_app.logger.info('DeliveryOfficerRepository full retrival')
        return dos 
    
    def select_one(self,id:int)->Any:
        dos = self.db.session.query(DeliveryOfficer).filter(DeliveryOfficer.id==id).one_or_none()
        current_app.logger.info('DeliveryOfficerRepository retrival by id')
        return dos 

