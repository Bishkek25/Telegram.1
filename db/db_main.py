
import sqlite3
from db import queries

db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()

async def sql_create():
    if db:
        print('База данных подключна!')
    cursor.execute(queries.CREAT_TABLE_STORE)
    cursor.execute(queries.CREATE_collection)

async def sql_insert_store(name_product, product_id, size, price, photo):
    cursor.execute(queries.INSERT_STORE,(name_product , product_id, size, price, photo))

    db.commit()

async def sql_insert_collection(product_id, collection):
    cursor.execute(queries.INSERT_collection,(product_id, collection))

    db.commit()


# async def sql_insert_store_detail(info_product, product_id, category_id):
#     cursor.execute(queries.INSERT_INTO_STORE_DETAIL,(info_product, product_id, category_id))
#
#     db.commit()