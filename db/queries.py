
CREAT_TABLE_STORE = """
CREATE_TABLE IF NOT EXISTS store ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product TEXT,
    product_id TEXT,
    size TEXT,
    price TEXT,
    photo
)
"""

CREATE_collection = """
CREATE_TABLE IF NOT EXISTS collection_products ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id TEXT,
    collection TEXT
)
"""



INSERT_STORE ="""
     INSERT INTO_store (name_product, product_id, size, price, photo)
     VALUES (?, ?, ?, ?, ?)
"""

INSERT_collection ="""
     INSERT INTO_collection_products (product_id, collection)
     VALUES (?, ?)
"""







CREAT_TABLE_TABLE_DETAIL = """
CREAT TABLE IF NOT EXISTS store_detail (
id INTEGER PRIMARY KEY AUTOINCREMENT,
info_product TEXT,
product_id TEXT,
category_id TEXT,
)
"""

INSERT_STORE_DETAIL = """

       INSERT INTO_store_detail (info_product, product_id, category_id)
         VALUES (?, ?, ?)
"""



