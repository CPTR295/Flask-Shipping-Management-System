from flask import request,render_template,current_app
from modules.model.db import Customer
from modules.login import login_bp
from modules.login.repository.customer import CustomerRepository
from modules.login.services.login import get_login_id
from exceptions.db import DuplicateRecordException
from modules import db 

@login_bp.route('/customer/add',methods=['GET','POST'])
def add_customer():
    if request.method == 'POST':
        current_app.logger.info('add_customer POST View executed')
        cust = Customer(id=request.form['id'],firstname=request.form['firstname'],lastname=request.form['lastname'],
        middlename=request.form['middlename'],address=request.form['address'],mobile=request.form['mobile'],
        email=request.form['email'],status=request.form['status'])
        repo = CustomerRepository(db)
        res = repo.insert(customer=cust) 
        if res == False:
            raise DuplicateRecordException()
    
    current_app.logger.info('add_customer GET View executed')
    logins= get_login_id(2,db)
    return render_template('customer_details_form.html',logins=logins),200