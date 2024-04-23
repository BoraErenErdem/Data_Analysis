

import pandas as pd
import numpy as np
from os import path

# print(path.abspath('auto.csv'))

df = pd.read_csv('Data/auto.csv')
print(df.head().to_string())



# NOT: ML algoritmalarında her bir veri çok önemlidir. Eğer ne kadar çok veri ile ML algoritmaını train edilirse o kadar başarılı sonuçlar elde edilir. O yüzden ML algoritmaları için verilerin her biri bile çok önemlidir.




# region Veri setinde sütun isimleri yok. Veri setine sütun isimleri ekle.
df.columns = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
                "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight",
                "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio",
                "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]
print(df.head().to_string())
# endregion



# Eksik ve Hatalı Veriler
# Eksik ve hatalı verileri numpy kütüphanesinde bulunan NaN yani boş anlamına gelen veri ile değiştirmemiz gerekir. Böylece ML algoritmasında hata ile karşılaşmamış oluruz.

# region Datada ? gördüğün yere numpy'ın NaN ifadesini getir
df.replace(to_replace='?', value=np.nan, inplace=True)  # önce to_replace ile değiştirmek istediğimiz ifadeyi yazıyoruz.
print(df.to_string())                                               # sonra value ile yerine getireceğimiz ifadeyi yazıyoruz.
# endregion                                             # inplace=True ile de yeni bir değişkene atamak zorunda kalmadan df'in üzerine direkt kaydedebiliyoruz..!


# region Ne kadar eksik değerim var sapta
print(df.isnull().sum())  # isnull() fonksiyonu 'NaN' gördüğü hücrelere 'True' görmediği yerlere 'False' değeri basar. Burada sum() ekleyerek bütün NaN değerleri yani True dönen değerleri sütunlara göre topladık. Ayrıca isna() ile isnull() aynı işleve sahiptir.

print(df.isna().sum())  # isna() ile isnull() aynı işleve sahiptir.
# endregion


# region Kayıp veriler belirlendi şimdi onlarla başaçık.

# 1.Yol (Ortalama Değeri Bularak Eksik Veriler İle Değiştirme)
# İlgili sütunda bulunan değerlerin ortalamasını alarak bu ortalama değeri eksik değerlerin bulunduğu hücreye yani NaN olan yerlere yazdık.
df['normalized-losses'] = df['normalized-losses'].replace(to_replace=np.nan, value=df['normalized-losses'].astype(float).mean())  # astype() veri tipini dönüştürmek için kullanılır
print(df)

df['price'] = df['price'].replace(to_replace=np.nan, value=df['price'].astype(float).mean())
print(df['price'].to_string())


# 2.Yol (Frekans Aralığı İle Eksik Verileri Değiştirme)
# İlgili sütunda bulunan değerlerin frekans aralığını alarak yani sütunda ne sıklıkla bulunduğunu belirleyerek bulunduğu hücreye yani NaN olan yerlere yazdık.
df['num-of-doors'] = df['num-of-doors'].replace(to_replace=np.nan, value=df['num-of-doors'].value_counts().idxmax())  # idxmax() ilgili sütunda en çok geçen değeri verir
print(df['num-of-doors'].to_string())                                                                       # value_counts() bir sütunda geçen farklı değerlerin kaç tane olduğunu bize söyler

df['bore'] = df['bore'].replace(to_replace=np.nan, value=df['bore'].value_counts().idxmax())
print(df['bore'].to_string())
# endregion



# region Veri Standardizasyonu (Machine Learning)
# ML algoritmalarında kullanılacak değerlerin belirli bir standartta olması gerekir. Veri setindeki farklı birimlere sahip değerler ML algoritmasının train edip ürettiği sonuçları olumsuz etkiler. Bunun için verinin bir standartta olması çok önemlidir.
df['city_l/km'] = 235/df['city-mpg']
df['highway_l/km'] = 235/df['highway-mpg']
# endregion


# region Veri Normalizasyonu (Machine Learning)
# Belirli bir sütundaki değerlerin benzer bir aralığa kavuşması için yapılır. Daha küçük scaler büyüklüklere dönüşütürülür ve böylece belli ölçekte olmaları sağlanır.
df['length'] = df['length'] / df['length'].max()
df['width'] = df['width'] / df['width'].max()
df['height'] = df['height'] / df['height'].max()

print(df[['length', 'width', 'height']])
# endregion


# region Dummy Variable (Machine Learning)
# Sözel ya da kategorik değişkenlerin scaler büyüklüklere dönüştürmemizi sağlar.
dummy_variable_df = pd.get_dummies(df['fuel-type'], dtype=float)  # veri setinde 'fuel-type' sütununda kategorik değerler diesel, gas vb bulunmaktadır. Bunları scaler büyüklüklere dönüştürdük.
print(dummy_variable_df)                                          # get_dummies() str olan veri türünü int ya da floata dönüştürür
# endregion


# region bakım yapılan yeni veri setini excele yaz
df.to_csv('Data/clean_auto.csv')
# endregion