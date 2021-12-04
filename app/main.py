from fastapi import FastAPI
from cassandra.cqlengine.management import sync_table
from typing import List
import config,db,models,schema

settings = config.get_settings()
app = FastAPI()


@app.on_event("startup")
def on_startup():
    global session
    session = db.get_session()
    sync_table(models.Product)
    sync_table(models.ProductScrapeEvent)


@app.get("/")
def index():
    return {"data":"hello world","name":settings.name}

@app.get("/products",response_model=List[schema.ProductListSchema])
def prod_list_view():
    return list(models.Product.objects.all())


@app.get("/products/{asin}")
def prod_list_view(asin:str):
    data = dict(models.Product.objects.get(asin=asin))
    events = list(models.ProductScrapeEvent.objects.filter(asin=asin))
    data['events']=[schema.ProductDetailSchema(**x) for x in events]
    return data