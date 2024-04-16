

import pandas as pd
from os import path

# print(path.abspath("imdb.csv"))

# region ilk 5 ve son 5 satırı bul
df = pd.read_csv("Data/imdb.csv")
print(df)
# endregion


# region bütün satırları bul
df = pd.read_csv("Data/imdb.csv")
print(df.to_string())  # to_string() bütün satırları verir
# endregion


# region Movie_Title sütunun ilk 20 satırını df olarak ekrana bas

# 1.Yol
df = pd.read_csv("Data/imdb.csv")
print(df[['Movie_Title']].head(20))

# 2.Yol
print(df[['Movie_Title']][0:20])

# 3.Yol
print(df.loc[: 20, 'Movie_Title'])
# endregion


# region Filtre => Rating 7.0 ' dan büyük olan ve Select => Movie_Title, Rating, YR_Released

# 1.Yol
df = pd.read_csv("Data/imdb.csv")
result = df.query("Rating >= 7.0")[['Movie_Title', 'Rating', 'YR_Released']].sort_values("Rating")
print(result.to_string())

# 2.Yol
print(df[df['Rating'] >= 7.0][['Movie_Title', 'Rating', 'YR_Released']].sort_values("Rating", ascending=False).to_string())
# endregion


# region YR_Released bilgisi 2014 ile 2018 arasında olan filmlerin Title, Rating, YR_Released bilgilerini listeleyin

# 1.Yol
df = pd.read_csv("Data/imdb.csv")
result = df.query("2014 <= YR_Released <= 2018")[['Movie_Title', 'Rating', 'YR_Released']].sort_values("YR_Released")
print(result.to_string())

# 2.Yol
print(df[df['YR_Released'].between(2014, 2018)][['Movie_Title', 'Rating', 'YR_Released']].sort_values("YR_Released").to_string())
# endregion


# region Num_Reviews 100.000'den büyük yada Rating 8 ile 9 arasında olan filmlerin Movie_Title, Rating, YR_Released bilgilerini listeleyin

# 1.Yol
df = pd.read_csv("Data/imdb.csv")
result = df.query("Num_Reviews > 100 | 8 < Rating < 9")[['Movie_Title', 'Rating', 'YR_Released']].sort_values("Movie_Title")
print(result.to_string())

# 2.Yol
print(df[df['Num_Reviews'] > 100 | df['Rating'].between(8, 9)][['Movie_Title', 'Rating', 'YR_Released']].sort_values("Movie_Title").to_string())
# endregion


# region Runtime süresi 100'den büyük en uzun olan ilk 20 filmin Movie_ID, YR_Released, Rating, Runtime bilgilerini listele

# 1.Yol
print(df[df['Runtime'] > 100][['Movie_ID', 'YR_Released', 'Rating', 'Runtime']].sort_values("Runtime", ascending=False).head(20))

# 2.Yol
df = pd.read_csv("Data/imdb.csv")
result = df.query("Runtime > 100")[['Movie_ID', 'YR_Released', 'Rating', 'Runtime']].sort_values("Runtime", ascending=False).head(20)
print(result)
# endregion


# region son 5 satırını gösterin.
print(df.tail(5))
# endregion


# region Toplam film sayısını bul
print(df.shape)
# endregion


# region Rating sütununun ortalama değeri nedir

# 1.Yol
df = pd.read_csv("Data/imdb.csv")
print(df['Rating'].mean())

# 2.Yol
rating_ortalama = df['Rating'].mean()
print(rating_ortalama)
# endregion


# region En yüksek numaralı inceleme (Num_Reviews) sayısına sahip film hangisi
df = pd.read_csv("Data/imdb.csv")
result_max = df['Num_Reviews'].max()
max_movie_title = df.loc[df['Num_Reviews'] == result_max, 'Movie_Title'].iloc[0]
print(max_movie_title)
print(result_max)
# endregion


# region 2000 yılından sonra yayınlanan filmlerin sayısı nedir

# 1.Yol
df = pd.read_csv("Data/imdb.csv")
filmler_2000_sonrasi = df.query("YR_Released > 2000").shape[0]
print(filmler_2000_sonrasi)

# 2.Yol
print(f" 2000 Yılından Sonra Çıkan Filmler: {df[df['YR_Released'] > 2000].shape[0]}")
# endregion


# region Runtime sütununun standart sapması nedir?
print(df['Runtime'].std())
# endregion


# region 2.0'ın altında bir değere sahip olan filmlerin sayısı nedir

#1.Yol
print(df[df['Rating'] < 2.0].shape[0])

# 2.Yol
print(df.query('Rating < 2.0')[['Movie_Title', 'Rating']].to_string())
# endregion


# region Rating sütununu 2.0'den büyük ve Num_Reviews sütununu 10.000'den fazla olan filmleri filtrele.

# 1.Yol
df = pd.read_csv("Data/imdb.csv")
print(df.query("(Rating > 2.0) & (Num_Reviews >= 10000)").sort_values("Num_Reviews", ascending=False).to_string())

# 2.Yol
print(df[(df['Rating'] > 2.0) & (df['Num_Reviews'] >= 10000)].sort_values("Rating", ascending=False).to_string())
# endregion


# region Veri setindeki en yüksek puanlı 2 film hangisidir ve bu filmin puanı nedir

# 1.Yol
print(df[df['Rating'] == df['Rating'].max()][['Movie_Title','Rating']].drop_duplicates())

# 2.Yol
d = pd.read_csv("Data/imdb.csv")
result_max = df['Rating'].max()
result_max_film = df[df['Rating'] == result_max][['Movie_Title','Rating']].drop_duplicates()
print(f'En yüksek puan alan filmler: {result_max_film}')
print(f'Puan: {result_max}')
# endregion