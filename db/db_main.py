
import sqlite3
from itertools import product
import aiosqlite

from db import queries

db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()

async def sql_create():
    if db:
        print('База данных подключна!')
    cursor.execute(queries.CREAT_TABLE_STORE)
    cursor.execute(queries.CREATE_collection)
    cursor.execute(queries.CREAT_TABLE_TABLE_DETAIL)

async def sql_insert_store(name_product, product_id, size, price, photo):
    cursor.execute(queries.INSERT_STORE,(name_product , product_id, size, price, photo))

    db.commit()

async def sql_insert_collection(product_id, collection):
    cursor.execute(queries.INSERT_collection,(product_id, collection))

    db.commit()


async def sql_insert_store_detail(info_product, product_id, category_id):
    cursor.execute(queries.INSERT_STORE_DETAIL,(info_product, product_id, category_id))

    db.commit()

def get_db_connection():
    conn = sqlite3.connect('db/store.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn

def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""
        SELECT * FROM store s
INNER JOIN store_detail sd on s.product_id = sd.product_id
""").fetchall()

    conn.close()

    return products





