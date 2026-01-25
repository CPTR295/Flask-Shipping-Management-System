from flask import render_template,request,flash,session,current_app
from modules.model.db import Orders
from modules.order.repository.order import OrderRepository
from modules.login.services.customer import get_all_cid
from modules.product.services.product import get_all_pid

from modules.order import order_bp
from modules import db
from exceptions.db import DatabaseException 

@order_bp.route('/orders/add',methods=['GET',['POST']])
def add_order():
    if request.method == 'POST':
        current_app.logger.info('add_order POST view')
        repo = OrderRepository(db) 
        order = Orders(cid=int(request.form['cis']),pid=int(request.form['pid']),order_no=request.form['order_no'],
                       order_date=request.form['order_date'])
        res = repo.insert(order)
        if res == False:
            raise DatabaseException
        customers = get_all_cid(db) 
        products = get_all_pid(db)
        return render_template('add_order_form.html',customers=customers,products=products),200
    
    current_app.logger.info('add_order GET view')
    customers = get_all_cid(db=db)
    products = get_all_pid(db)
    return render_template('add_order_form.html',customers=customers,products=products)

@order_bp.route('/orders/list',method=['GET'])
def list_orders():
    repo = OrderRepository(db)
    orders = repo.select_all()
    flash('List of orders')
    return render_template('list_orders.html',orders=orders),200