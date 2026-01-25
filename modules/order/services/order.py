from modules.order.repository.order import OrderRepository

def get_all_orders_no(db):
    repo = OrderRepository(db) 
    ords = repo.select_all()
    ord_nos = [o.order_no for o in ords] 
    return ord_nos