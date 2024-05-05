

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt


movies_df = pd.read_csv('Data/movies.csv')
print(movies_df.head().to_string())

ratings_df = pd.read_csv('Data/ratings.csv')
print(ratings_df.head().to_csv())


movies_df['year'] = movies_df['title'].str.extract(r'(\W{1}\d{4}\W{1})', expand=False)
print(movies_df['year'])

movies_df['year'] = movies_df['year'].str.extract(r'(\d{4})', expand=False)
print(movies_df['year'])

movies_df['title'] = movies_df['title'].replace(to_replace=r'(\W{1}\d{4}\W{1})', value=' ', regex=True)
movies_df['title'] = movies_df['title'].apply(lambda x: x.strip())
print(movies_df['title'].head().to_string())


ratings_df.drop(['timestamp'], axis=1, inplace=True)
print(ratings_df.head().to_string())


user_input_df = pd.DataFrame([
    {'title': 'Toy Story', 'rating': 4},
    {'title': 'Jumanji', 'rating': 5},
    {'title': 'Father of the Bride Part II', 'rating': 5},
    {'title': 'Heat', 'rating': 1},
    {'title': 'Space Jam', 'rating': 5}
])


merged_user_input_df = pd.merge(user_input_df, movies_df, how='inner', on='title')
print(merged_user_input_df)

# region bu sefer 1995 olan Heat kalsın diğer Heatler silinsin
merged_user_input_df.drop([4,5], axis=0, inplace=True)

merged_user_input_df.drop(['year'], axis=1, inplace=True)

merged_user_input_df.reset_index(drop=True, inplace=True)

print(merged_user_input_df.to_string())


# yeni gelen kullanıcı hali hali hazırda aynı filmleri rate etmiş kullanıcıları saptayalım
user_subset_df = pd.merge(ratings_df, merged_user_input_df, how='inner', on='movieId')
print(user_subset_df.head().to_string())

user_subset_df.drop(['rating_y', 'title'], axis=1, inplace=True)
print(user_subset_df.head().to_string())

user_subset_df.rename(columns={'rating_x':'rating'}, inplace=True)
print(user_subset_df.head().to_string())


# artık user_subset_df içerisinde yeni gelen kullanıcı ile aynı filmleri rate etmiş kullanıcılar var
# user_id'lerine göre ilgili veri setini gruplayalım

user_subset_group = user_subset_df.groupby('userId')

# for name, group in user_subset_group:  # bütün user_subset_group'takileri sıralar
#     print(f'Group Name: {name}\n'
#             f'Group: {group}')


# yukarıda elde ettiğimiz veri kelimesini sort edelimki yeni gelen kullanıcın rate ettiği filimlerle aynı sırada aynı filmleri rate etmiş kullanıcıları saptayalım
sorted_user_subset_group = sorted(user_subset_group, key=lambda x: len(x[1]), reverse=True)  # listenin ikinci elemanının (yani filmlerin listesinin) uzunluğuna göre sıralama yapar

print(sorted_user_subset_group[1])


# Bu kısımda yeni gelen kullanıcı ile bu kullanıcının rate ettiği filmleri hali hazırda rate etmiş kullanıcılar arasındaki kolerasyonu bulacağız. Burada kolerasyon ile kullanıcılar arasındaki ilişkiyi inceleyeceğiz aslında ilişkiyi ortaya koyacağız. Korelasyon istatistik biliminde yoğun olarak kullanılmaktadır ve farklı kolerasyon türleri bulunmaktadır. Biz burada pearson kolerasyonu kullanacağız.

# kolerasyon sonucunu store etmek için bir dictionary yaratalım
pearson_correlation_dict = {}

for user, group in sorted_user_subset_group:
    # group girdisi ile  user_input_df her iki tarafta bulunan movieId sütununa göre sıralıyoruz. Böylece değerler daha sonra birbirine karışmayacak nizami bir sıralama elde edeceğiz.
    group.sort_values('movieId', inplace=True)
    merged_user_input_df.sort_values('movieId', inplace=True)

    # pearson kolerasyonunu hesaplamak için kullanılan formülü burada belirtmemiz gerekecek bu yüzden formülde bulunan N katsayısnı tanımlıyoruz.
    n_rating = len(group)

    # merge işlemi yaparken merge etme şeklimizden bazı gereksiz sütunlar elde ediyoruz. alternatif bir yöntem ile merge işlemi yapacağız.
    # grouplar içerisindeki movieId ile user_input_df'teki movieIdleri kullanarak veri setlerini birleştiriyoruz. unutmayın yukarıda iki veri setini aynı hizaya soktuk. ilk yaptığımız işlem oydu şimdi ise birleştiriyoruz.

    temp_df = merged_user_input_df[merged_user_input_df['movieId'].isin(group['movieId'].tolist())]  # dataframe'den seçili sütunla isin()'e yazdığımız sütunu karşılaştırır True ise yazdırır False ise es geçer.
    # print(temp_df.to_string())

    # pearson korelasyonundaki argümanlarda kullanılmak üzere rating bilgilerini elde ediyorum.
    temp_rating_list = temp_df['rating'].tolist()
    temp_group_list = group['rating'].tolist()

    # bu ana kadar korelasyon formülünü uygulamak için ihtiyaç duyulan argümanların hazırlığını yaptık şimdi x ve y olarak nitelendireceğimiz iki attribute arasındaki benzerliği bulacağız.
    Sxx = sum([i ** 2 for i in temp_rating_list]) - pow(sum(temp_rating_list), 2) / float(n_rating)
    Syy = sum([i ** 2 for i in temp_group_list]) - pow(sum(temp_group_list), 2) / float(n_rating)

    Sxy = sum(i * j for i, j in zip(temp_rating_list, temp_group_list)) - sum(temp_rating_list) * sum(temp_group_list) / float(n_rating)

    if Sxx != 0 and Syy != 0:
        pearson_correlation_dict[user] = Sxy / sqrt(Sxx * Syy)
    else:
        pearson_correlation_dict[user] = 0

# print(pearson_correlation_dict)

pearson_df = pd.DataFrame.from_dict(pearson_correlation_dict, orient='index')  # orient= 'index' ifadesi Dataframe'in indexleri oldu
# print(pearson_df.head().to_string())
pearson_df.columns = ['similarity index']  # kolerasyon sonucu elde ettiğimiz ilişki ağırlığını yeni sütun olarak belirttik
pearson_df['userId'] = pearson_df.index  # 'userId' sütununundaki verileri ayrıca index olarak atadık
pearson_df.reset_index(drop=True, inplace=True)  # indexleri sıfırladık yani resetleyip yazdırdık
sorted_pearson_df = pearson_df.sort_values('similarity index', ascending=False)
# print(sorted_pearson_df.head(100).to_string())
top_user_rating_df = sorted_pearson_df.merge(ratings_df, how='inner', on='userId')
# print(top_user_rating_df.head(100).to_string())
top_user_rating_df['weigthed rating'] = top_user_rating_df['similarity index'] * top_user_rating_df['rating']

temp_user_rating = top_user_rating_df.groupby('movieId').sum()[['similarity index', 'weigthed rating']]

temp_user_rating['recomandation score'] = temp_user_rating['weigthed rating'] / temp_user_rating['similarity index']

temp_user_rating = temp_user_rating.sort_values('recomandation score', ascending=False)

recomandation_df = pd.merge(temp_user_rating, movies_df, how='inner', on='movieId')

sorted_recomandation_df = recomandation_df.sort_values('similarity index', ascending=False)

print(sorted_recomandation_df.head(20).to_string())