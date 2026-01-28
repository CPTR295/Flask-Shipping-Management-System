from flask import render_template,request,flash,abort,current_app
from modules.model.db import Payment,PaymentType
from modules.payment.repository.payment import PaymentRepository , PaymentTypeRepository
from modules.order.services.order import get_all_orders_no
from modules.payment import payment_bp 
from modules import db 

@payment_bp.route('/payment/type/add',methods=['GET','POST'])
def add_payment_type():
    if request.method=='POST':
        current_app.logger.info('add_payment_type post view')
        payt = PaymentType(name=request.form['name'])
        repo = PaymentTypeRepository(db) 
        res = repo.insert(payt)
        if res==False:
            abort(500) 
        return render_template('add_payment_scheme_form.html'),200
    current_app.logger.info('add_payment_type get view')
    return render_template('add_payment_scheme_form.html'),200

@payment_bp.route('/payment/add',methods=['GET','POST'])
def add_payment():
    if request.method == 'POST':
        current_app.logger.info('add_payment post view')
        pay = Payment(order_no=request.form['order_no'],mode_payment=request.form['mode_payment'],
                      ref_no=request.form['ref_no'],date_payment=request.form['date_payment'],amount=request.form['amount'])
        repo = PaymentRepository(db) 
        repot = PaymentTypeRepository(db) 
        payts = repot.select_all()
        orders = get_all_orders_no(db) 
        res = repo.insert(pay)
        if res==False:
            abort(500) 
        return render_template('add_payment_form.html',orders=orders,ptypes=payts),200
    current_app.logger.info('add_payment Get view')
    repot = PaymentTypeRepository(db) 

    payts = repot.select_all() 
    
    orders = get_all_orders_no(db) 
   
    return render_template('add_payment_form.html',orders=orders,ptypes=payts),200

@payment_bp.route('/payment/list',methods=['GET'])
def list_payment():
    repo=PaymentRepository(db) 
    print(1)
    pays = repo.select_all() 
    print(2)
    flash('List of payments') 
    print(3)
    return render_template('list_payments.html',payments=pays),200