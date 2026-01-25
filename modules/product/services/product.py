from modules.product.repository.product import ProductRespository

def get_all_pid(db):
    repo = ProductRespository(db)
    recs = repo.select_all()
    ids=[(p.id,p.name) for p in recs]
    return ids