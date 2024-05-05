

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from os import path


movies_df = pd.read_csv('Data/movies.csv')
print(movies_df.head().to_string())

ratings_df = pd.read_csv('Data/ratings.csv')
print(ratings_df.head().to_string())





# NOT: str.extract() methodu Pandas Serilerinde metin verilerinden regex kullanarak aranılan ya da ayıklanmak istenen ifadeyi çıkarır.

# region movies_df içindeki title sütununda yer alan yıl bilgilerini parantezleriyle birlikte söküp al. Sonra year sütunu açıp parantezsiz şekilde sütuna yazdır. regex kullan.
movies_df['year'] = movies_df['title'].str.extract(pat=r'(\W{1}\d{4}\W{1})', expand=False)  # burada regex kullanarak parantezleriyle birlikte yıl bilgilerini söküp year sütununna atadık.
print(movies_df['year'])  # W{} kaç tane sembol var, d{} kaç tane art arda sayı var, s{} kaç tane boşluk var onları temsil eder.

movies_df['year'] = movies_df['year'].str.extract(pat=r'(\d{4})', expand=False)  # sadece art arda 4 tane sayı gelenleri aldık böylece yıl bilgilerini parantezden kurtardık.
print(movies_df['year'])  # expand=True olursa Dataframe döner. expand=False olursa Seri döner.

movies_df['title'] = movies_df['title'].replace(to_replace=r'(\W{1}\d{4}\W{1})', value=' ', regex=True)  # regex=True ifadesi regex kullandığımızı gösterir.
print(movies_df['title'])  # burada title içindeki yıl ifadesi bulunan yerleri sildik ve yerine boşluk koyduk

movies_df['title'] = movies_df['title'].apply(lambda x: x.strip())  # .strip() fonksiyonu bulduğu boşluğu siler
print(movies_df.head().to_string())  # burada title sütunundaki boşluk koyduğumuz yerleri sildik
# endregion


# region movies_df'in kopyasını oluştur
movies_copy_df = movies_df.copy()
# endregion


# region genres listesi oluştur ama her bir tür bir kez içerisinde bulunsun.
movies_genres_listesi = []
for index, column in movies_df.iterrows():
    for i in column['genres'].split('|'):
        movies_genres_listesi.append(i)


unique_genres = np.unique(movies_genres_listesi)  # tekrarlanan türleri yazmamasını sağladık
unique_genres = np.delete(unique_genres, [0])  # işimize yaramayacak olan baştaki indexsi sildik
print(unique_genres)
# endregion


# region Yukarıda elde ettiğimiz movies_genres_listesi'nin her bir itemi için movies_genres_df içinde bir sütun yarat. sütunların değerlerine NaN bas. pandas içerisinde assign() fonksiyonu kullan.
movies_copy_df = movies_copy_df.assign(**{column: np.nan for column in unique_genres})  # assign() fonksiyonu tekrarlanan fonksiyonları 1 kere yazdırırdığı için dict olarak dict compherisation verip yaz. ** sınırsız argüman demek birden fazla olduğu için ** verdik
print(movies_copy_df.head().to_string())
# endregion


# region yeni yarattığımız ayrı ayrı tür sütunlarına 1, film bir türe sahip değilse 0 basılsın
for index,column in movies_df.iterrows():
    for i in column['genres'].split('|'):
        movies_copy_df.loc[index, i] = 1  # movies_df_copy DataFrame'inde, o anki satırın ve o satırın 'genres' sütunundan elde edilen türün olduğu sütuna 1 değeri atanır. Yani, film o türe sahipse, ilgili sütuna 1 atanır.

movies_copy_df.fillna(0, inplace=True)  # fillna() DataFrame'deki eksik değerleri belirtilen bir değerle doldurmak için kullanılır.
print(movies_copy_df.head().to_string())
# endregion


# region sisteme yeni üye olmuş kullanıcının rate ettiği filmlerin datası var. bu veri setinde filmlerin id'leri genresları bulunmamaktadır. bu bilgilerinde olacağı bir df oluşturalım. yani bu bilgileri merge et.
user_input_df = pd.DataFrame([
    {'title': 'Toy Story', 'rating': 4},
    {'title': 'Jumanji', 'rating': 5},
    {'title': 'Father of the Bride Part II', 'rating': 5},
    {'title': 'Heat', 'rating': 1},
    {'title': 'Space Jam', 'rating': 5}
])

print(user_input_df)


birlesmis_user_input_df = pd.merge(user_input_df, movies_df, how='inner', on='title')
print(birlesmis_user_input_df.to_string())
# endregion


# region türleri ==> Comedy|Drama|Romance olan Heat filmlerini silelim yani sadece 1972 olan  Heat kalsın.
birlesmis_user_input_df.drop([3,5], axis=0, inplace=True)
print(birlesmis_user_input_df.to_string())
# endregion


# region genres ve year sütunlarını da sil.
birlesmis_user_input_df.drop(['genres', 'year'], axis=1, inplace=True)
print(birlesmis_user_input_df.to_string())
# endregion


# region yukarıdaki index silme işlemi yüzünden index bozuldu birlesmis_user_input_df indexlerini sıfırla. (yani resetle)
birlesmis_user_input_df.reset_index(drop=True, inplace=True)
print(birlesmis_user_input_df)
# endregion


# region user'in rate ettiği filmlerin id'lerini yukarıda saptadık. şimdi bu filmlerin sahip oldukları türlerin veri setini oluşturalım.
user_favorite_genres = pd.merge(birlesmis_user_input_df, movies_copy_df ,how='inner', on='movieId')
print(user_favorite_genres.to_string())

user_favorite_genres.drop(['title_y', 'title_x', 'rating', 'movieId', 'year', 'genres'], axis=1, inplace=True)
print(user_favorite_genres.to_string())
# endregion


# region user_profile oluştur series olsun
user_profile = user_favorite_genres.transpose().dot(user_input_df['rating'])  # .dot() matris çarpımı yapmak için kullanılır. matris çarpımı yapabilmek için transpose ettik.
print(user_profile)
# endregion


# region movie_matrix oluşturalım
movies_matrix = movies_copy_df.drop(['title', 'genres', 'year'], axis=1)
movies_matrix.set_index('movieId', inplace=True)
print(movies_matrix.head().to_string())
# endregion


# region recommendation matrix oluşturalım
recommendation_matrix = pd.DataFrame((movies_matrix * user_profile).sum(axis=1) / user_profile.sum())

recommendation_matrix.columns = ['Weighted Average']

print(recommendation_matrix.sort_values('Weighted Average', ascending=False).head().to_string())

result_df = pd.merge(movies_df, recommendation_matrix, how='inner', on='movieId')
print(result_df.sort_values('Weighted Average', ascending=False, inplace=True))
# endregion

result_df.head(20).plot(x='title', y='Weighted Average', kind='bar')
plt.show()