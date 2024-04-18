

import pandas as pd
import numpy as np
from os import path


# region Pandas Series Entry_Lvl examples

sayilar = [10, 20, 30,  40]

pd_series = pd.Series(sayilar)
print(pd_series)
print(type(pd_series))

sozluk = {
    'a': 10,
    'b': 20,
    'c': 30
}

pd_series = pd.Series(sozluk)
print(pd_series)
print(type(pd_series))

print(pd_series[:2])  # pandas serilerinde slicing işlemi


# pandas serilerindeki built-in fonksiyonlar
print(pd_series.shape)  # serini kaç satır ve sütun olduğunu gösterir  # NOT: reshape() fonksiyonu veriyi yeniden şekillendirmek için kullanılırken, shape özelliği bir veri yapısının boyutunu kontrol etmek için kullanılır.


print(pd_series.dtypes)  # serinin veri tipini döndürür
print(pd_series.ndim)  # serinin kaç katmanlı olduğuna bakar
print(pd_series.describe())  # serinin özet bilgilerini verir
print(pd_series.head(1))  # ilk indexten başlayarak verilen indexe kadar olan indexleri döndürür. Eğer içine argüman yazılmazsa ilk 5 satırı yazdırır.
print(pd_series.tail(1))  # son indexten başlayarak verilen indexe kadar olan indexleri döndürür. Eğer içine argüman yazılmazsa son 5 satırı yazdırır.

# Aggregate function'ları kullanabiliriz. ( sum(), mean(), count(), max() .....)
print(f'Bütün indexler toplamı = {pd_series.sum()}')


# pandas indexe göre toplama yapar
Yamaha2020 = pd.Series([20, 30, 40], ['R7', 'Tracer', 'MT'])
Yamaha2023 = pd.Series([50, 60, 70], ['Tracer', 'MT', 'R7'])

toplam = Yamaha2020 + Yamaha2023

print(toplam)
# endregion



# region Pandas DataFrame Entry_Lvl examples
# DataFrame'de daha çok satır ve sütunlardan oluşan yapılar kullanıcaz
df = pd.DataFrame(
    data=np.random.rand(4, 5),
    index=['Bora', 'Burak', 'Akif', 'Cem'],
    columns=['Sütun1', 'Sütun2', 'Sütun3', 'Sütun4', 'Sütun5']
)

print(df)

print(df['Sütun2'])
print(type(df['Sütun2']))  # DataFrame Serilerden oluşur. Yani DataFrame'den seri alabilirsin.

print(df[['Sütun1']])
print(type(df[['Sütun1']]))  # [[]] parantezden dolayı tipi DataFrame olarak verdi.

print(df.loc['Bora'])  # index değeri verip o indexte tutulan veriye erişebilirsin
print(df.loc[['Bora']])  # DataFrame olarak verir çıktı verir [[]]

print(df.loc['Burak', 'Sütun5'])
print(df.loc[['Bora', 'Burak'], ['Sütun1', 'Sütun2']])
print(df.loc[:, ['Sütun1', 'Sütun3']])  # sadece sütun vermesini istiyorsak : koyup , atıp yazdığında index bölümünü geçip sütun bölümünü yazdırmış olursun


# NOT: iloc[] methodu eğer indeximizi sayı olarak değil başka türlü verdiysek fakat yine de sayı indexine göre belirtmek istiyorsak iloc() kullanabiliriz.
print(df.iloc[2])  # Akif indexindeki bilgileri bize verir.


# Yeni Sütun ekleme
df['Sütun6'] = pd.Series(np.random.rand(4), ['Bora', 'Burak', 'Akif', 'Cem'])  # Ekleyeceğimiz sütunun datasını ve indexlerini verdik

df['Sütun7'] = df['Sütun1'] + df['Sütun2']  # Ekleyeceğimiz sütun iki sütunun toplamı olabilir


# Sütun silme
df.drop('Sütun7', axis=1)  # DataFrame'de sütun silmek istediğimizde axisini vermemiz gerekiyor. axis = 1 ise Y ekseni yani yukardan aşağıya siler. axis = 0 ise X ekseni yani sağdan sola siler. Ayrıca bu işlemi bir değişkene atamazsak orjinal DataFrame'de bir değişiklik olmaz.
print(df)

result = df.drop('Sütun7', axis=1)  # Bu işlemde değişkene atadığımız için artık DataFramemiz değişti.
print(result)
# endregion