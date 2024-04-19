

import pandas as pd
import numpy as np



customers = {
    'CustomerId': [1,2,3,4],
    'FirstName': ['Ahmet', 'Ali', 'Hasan', 'Canan'],
    'LastName': ['Yılmaz', 'Korkmaz', 'Çelik', 'Toprak']
}


orders = {
    'OrderId': [10,11,12,13],
    'CustomerId': [1,2,5,7],
    'OrderDate': ['2010-07-04', '2010-08-04', '2010-07-07', '2012-07-04']
}

df_customers = pd.DataFrame(customers)
df_orders = pd.DataFrame(orders)

print(df_customers)
print(df_orders)


# inner merge (kesişimlerini almak)
print(pd.merge(df_customers, df_orders, how='inner', on='CustomerId'))

# left merge (soldakileri almak)
print(pd.merge(df_customers, df_orders, how='left', on='CustomerId'))

# right merge (sağdakileri almak)
print(pd.merge(df_customers, df_orders, 'right'))

# outer (sağ ve soldakileri yani hepsini almak)
print(pd.merge(df_orders, df_customers, how='outer'))



customersA = {
    'CustomerId': [1,2,3,4],
    'FirstName': ['Ahmet', 'Ali', 'Hasan', 'Canan'],
    'LastName': ['Yılmaz', 'Korkmaz', 'Çelik', 'Toprak']
}


customersB = {
    'CustomerId': [4,5,6,7],
    'FirstName': ['Yağmur', 'Çınar', 'Cengiz', 'Can'],
    'LastName': ['Bilge', 'Turan', 'Yılmaz', 'Turan']
}


df_customersA = pd.DataFrame(customersA)
df_customersB = pd.DataFrame(customersB)

# concat (birleştirme işlemi)
print(pd.concat([df_customersA, df_customersB], axis=0))  # burada birleştirme işleminde axis=0 dersek satır (row) bazlı birleştirir
print(pd.concat([df_customersA, df_customersB], axis=1))  # burada birleştirme işleminde axis=1 dersek sütun (column) bazlı birleştirir

print(pd.merge(df_customersA, df_customersB, how='inner', on='CustomerId'))
print(pd.merge(df_customersA, df_customersB, 'outer'))  # sağ ve soldaki yani bütün kayıtları getirir
