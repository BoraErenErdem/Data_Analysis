

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('Data/forbes_2022_billionaires.csv')
print(df.head().to_string())


# region Bütün NaN olan değerleri sütunlara göre toplam kaç tane olduğunun sayısını göster
print(df.isnull().sum())
# endregion


# region Kayıp verilerin hepsini onar.

# region age sütununu onar
df['age'] = df['age'].replace(to_replace=np.nan, value=df['age'].astype(float).mean())
print(df['age'].to_string())
# endregion


# region country sütununu onar
df['country'] = df['country'].replace(to_replace=np.nan, value=df['country'].value_counts().idxmax())
print(df['country'].to_string())
# endregion


# region state sütununu onar
df['state'] = df['state'].replace(to_replace=np.nan, value=df['state'].value_counts().idxmax())
print(df['state'].to_string())
# endregion


# region city sütununu onar
df['city'] = df['city'].replace(to_replace=np.nan, value=df['city'].value_counts().idxmax())
print(df['city'].to_string())
# endregion


# region organization sütununu onar
df['organization'] = df['organization'].replace(to_replace=np.nan, value=df['organization'].value_counts().idxmax())
print(df['organization'].to_string())
# endregion


# region gender sütununu onar
df['gender'] = df['gender'].replace(to_replace=np.nan, value=df['gender'].value_counts().idxmax())
print(df['gender'].to_string())
# endregion


# region birthDate sütununu onar
df['birthDate'] = df['birthDate'].replace(to_replace=np.nan, value=df['birthDate'].value_counts().idxmax())
print(df['birthDate'].to_string())
# endregion


# region title sütununu onar
df['title'] = df['title'].replace(to_replace=np.nan, value=df['title'].value_counts().idxmax())
print(df['title'].to_string())
# endregion


# region philanthropyScore sütununu onar
df['philanthropyScore'] = df['philanthropyScore'].replace(to_replace=np.nan, value=df['philanthropyScore'].astype(float).mean())
print(df['philanthropyScore'].to_string())
# endregion


# region residenceMsa sütununu onar
df['residenceMsa'] = df['residenceMsa'].replace(to_replace=np.nan, value=df['residenceMsa'].value_counts().idxmax())
print(df['residenceMsa'].to_string())
# endregion


# region numberOfSiblings sütununu onar  ??????? Tam sayıya yuvarlamam gerekir mi S O R ??????
df['numberOfSiblings'] = df['numberOfSiblings'].replace(to_replace=np.nan, value=df['numberOfSiblings'].astype(float).mean())
print(df['numberOfSiblings'].to_string())
# endregion


# region about sütununu onar  ???? Burada her kişinin about kısmı farklı olması gerekmez mi neden frekansını alıyoruz S O R ??????
df['about'] = df['about'].replace(to_replace=np.nan, value=df['about'].value_counts().idxmax())
print(df['about'].to_string())
# endregion

# endregion


# region sütunların tiplerini göster
for i in df.columns:
    print(type(i))
# endregion


# region personName sütunun index olarak ayarla
df.set_index('personName', inplace=True)
print(df.head().to_string())
# endregion


# region veri setindeki bütün parasal değerlerin ortalamasını bul
print(df['finalWorth'].mean())
# endregion


# region en çok servete sahip olan kişinin serveti ve adı nedir
print(f'En çok servete sahip olan kişinin ismi: {df['finalWorth'].idxmax()}')
print(f'En çok servete sahip olan kişinin serveti: {df['finalWorth'].max()}')
# endregion


# region Yaşı 50 ve üstünde olanların adını ve finalWorth değerini getir ve yaşa göre sırala
print(df[df['age'] >= 50][['age', 'finalWorth']].sort_values('age', ascending=False).to_string())
# endregion


# region gender F olanları göster
print(df[df['gender'] == 'F'][['age', 'source']].sort_values('age', ascending=False))
# endregion


# region philanthropyScore en yüksek olan kişilerin source ve country'sini bul
# 1.Yol
print(df[df['philanthropyScore'] == df['philanthropyScore'].max()][['source', 'country', 'philanthropyScore']].sort_values('philanthropyScore', ascending=False).to_string())

# 2.Yol
print(df.groupby(['source', 'country'])[['philanthropyScore']].max().sort_values('philanthropyScore', ascending=False).head())
# endregion


# region philanthropyScore en düşük olan kişilerin source ve country'sini bul
# 1.Yol
print(df[df['philanthropyScore'] == df['philanthropyScore'].min()][['source', 'country', 'philanthropyScore']].sort_values('philanthropyScore', ascending=False).to_string())

# 2.Yol
print(df.groupby(['source', 'country'])[['philanthropyScore']].min().sort_values('philanthropyScore', ascending=False).tail().to_string())
# endregion


# region source_sayici sütunu açarak 2 veya daha fazla olan kişileri göster
def source_sayici(source):
    return source.count(',')

df['source_sayici'] = df['source'].apply(source_sayici)

print(df[df['source_sayici'] >= 2][['source', 'country', 'category', 'age']].sort_values('age', ascending=False).head().to_string())
# endregion


# region Kaç farklı category vardır
print(df.groupby('category')[['category']].value_counts().drop_duplicates().count())
# endregion


# region En çok ortak yaşanılan country'i göster
print(df['country'].value_counts().head(1))
# endregion


# region SpaceX hakkında bilgileri göster
# 1.Yol
def SpaceX_bulucu(source):
    if 'SpaceX' in source:
        return True
    else:
        return False

result = (df[df['source'].apply(SpaceX_bulucu)][['bio']].sort_values('bio', ascending=False).to_string())
print(result)

# 2.Yol
print(df[df['source'].str.contains('SpaceX')][['bio']].sort_values('bio', ascending=False).to_string())  # str.contains() methoduyla source sütununda SpaceX var mı yok mu bulup yazdırdık
# endregion


# region en yaşlı 2 insanı isimlerine göre listele
print(df.groupby('age').idxmax().sort_values('age', ascending=False).head(2))
# endregion


# region Amazon şirketini kim kurmuştur
print(df[df['source'].str.contains('Amazon')][['age']].sort_values('age',ascending=False).head(1))
# endregion


# region about, bio ve numberOfSiblings sütunlarını sil
df.drop(['numberOfSiblings', 'bio', 'about'], axis=1, inplace=True)
print(df.head().to_string())
# endregion


# region Hangi ülkede en fazla milyarder var
print(df['country'].value_counts().sort_values(ascending=False))
# endregion


# region Hangi sektörde en fazla milyarder var
print(df['category'].value_counts())
# endregion


# region Veri setindeki ülkelerin en zengin milyarderlerinin sayısını karşılaştırmak için bir çubuk grafik oluştur
df_ulkelerdeki_milyarderler = df.groupby('country')[['country']].value_counts().sort_values(ascending=False)
print(df_ulkelerdeki_milyarderler)

df_ulkelerdeki_milyarderler.plot(kind='bar', stacked=False, alpha=0.75, figsize=(10,7))
plt.suptitle('Ülkelerdeki Milyarderler Sayısının Çubuk Grafiği', color='r')
plt.ylabel('Milyarder Sayısı', color='r')
plt.xlabel('Ülkeler', color='r')
plt.legend(labels= df_ulkelerdeki_milyarderler.index, prop={'size': 10})
plt.show()
# endregion


# region Normalizasyon, Standartizasyon ve Dummy Variable Uygulamaları

# region finalWorth sütununu Normalizasyon yap
df['finalWorth'] = df['finalWorth'] / df['finalWorth'].max()
print(df['finalWorth'])
# endregion


# region age sütununua Normalziasyon yap
df['age'] = df['age'] / df['age'].max()
print(df['age'])
# endregion


# region category sütununu dummy variable değişkenine dönüştür
df_dummy_variable = pd.get_dummies(df['category'], dtype=float)
print(df_dummy_variable)
# endregion


# region philanthropyScore sütununu Normalizasyon yap
df['philanthropyScore'] = df['philanthropyScore'] / df['philanthropyScore'].max()
print(df['philanthropyScore'])
# endregion


# region title sütununu dummy variable uygula
df_dummy_variable_title = pd.get_dummies(df['title'], dtype=float)
print(df_dummy_variable_title)
df_dummy_variable_title.value_counts().drop_duplicates()
# endregion

# endregion


# region Hangi ülkelerdeki milyarderlerin servetinin değeri en az
print(df.groupby('country')[['finalWorth']].mean().sort_values('finalWorth',ascending=False).tail(1))
# endregion


# region En çok milyarder hangi kategoriye ait bunu pasta grafiğinde göster
df_category = df['category'].value_counts()

df_category.plot(kind='pie', stacked=False, figsize=(10,7), autopct='%1.1f%%', pctdistance= 1.1, explode=[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1], shadow=True, labels=None)
plt.axis('equal')
plt.suptitle('Kategoriye Göre Milyarder Sayısının Pasta Grafiği', color='r')
plt.legend(df_category.index, prop={'size':5})
plt.show()
# endregion


# region Ülkelere göre milyarderlerin ortalama servetlerini karşılaştır ve bunu histogram ile göster
df_ortalama_servet = df.groupby('country')[['finalWorth']].mean().sort_values('finalWorth',ascending=False)
print(df_ortalama_servet)

count, bin_edges = np.histogram(df_ortalama_servet, bins=10)
print(count)
print(bin_edges)

df_ortalama_servet.plot(kind='hist', stacked=False, alpha=0.45, figsize=(10,7))
plt.suptitle('Ülkelere göre milyarderlerin ortalama servetlerinin histogram grafiği'.upper(), color='black')
plt.ylabel('Ortalama Servet', color='black')
plt.xlabel('Ülkeler', color='black')
plt.grid()
plt.show()
# endregion


# region Milyarderlerin cinsiyetlerine göre servet dağılımı nasıl bunu Kutu grafiğiyle göster
df_gender_finalWorth = df.groupby('gender')[['finalWorth']].count()
print(df_gender_finalWorth)

df_gender_finalWorth.plot(kind='box', stacked=False, figsize=(10,7), color='green')
plt.suptitle('Cinsiyetlere Göre Servet Dağılımı', color='r')
plt.ylabel('Milyarder Sayısı', color='r')
plt.xlabel('Cinsiyet',color='r')
plt.legend(df_gender_finalWorth.index, prop={'size': 8})
plt.show()
# endregion


# region Milyarderlerin yaş ortalaması nedir?
print(df['age'].mean())
# endregion


# region Farklı kategorilere ait milyarderlerin yaş ortalamalarını nokta nokta göster
df_category_age_mean = df.groupby('category')[['age']].mean().sort_values('age', ascending=False)
print(df_category_age_mean)

plt.figure(figsize=(10,7))  # bu grafik türünü .plot() diyip içine yazamayız. Bu grafik türünde dışına figsize yazıp sonra alta geçip .scatter() yazıp içine x ve y eksenini yazmamız gerekir.
plt.scatter(df_category_age_mean.index, df_category_age_mean['age'], color='blue')
plt.title('Kategorilere Göre Yaş Ortalamaları')
plt.ylabel('Yaş Ortalaması')
plt.xlabel('Kategori')
plt.xticks(rotation=45)  # x eksenindeki etiketlerin yönünü  45 dereceye ayarladık
plt.grid()
plt.show()
# endregion


# region Hangi kategorideki milyarderlerin toplam serveti en yüksek alan grafiğinde göster
df_category_total = df.groupby('category')[['finalWorth']].sum().sort_values('finalWorth',ascending=False)
print(df_category_total)

df_category_total.plot(kind='area', stacked=False, alpha=0.65, figsize=(10,7))
plt.suptitle('Kategoriye Göre Toplam Servetler', color='r')
plt.xlabel('Kategoriler', color='r')
plt.ylabel('Toplam Servet', color='r')
plt.xticks(rotation=45)
plt.show()
# endregion


# region yaş ve servet sütunu ikilisinin nokta grafiğini oluştur
plt.figure(figsize=(10,7))
plt.scatter(df['age'], df['finalWorth'], color='green')
plt.grid()
plt.show()
# endregion


# region Bu milyarderlerin %10'u en fazla hangi 2 sektörde yer almaktadır
df['category'].value_counts()
len(df)
category_percentage = (df['category'].value_counts() / len(df)) * 100
print(category_percentage.sort_values(ascending=False).head(2))
# endregion


# region En genç ve en yaşlı milyarderler kimler scatter ile göster
df['age'].idxmin()
df['age'].idxmax()

plt.figure(figsize=(10,7))
plt.scatter(df['age'].idxmin(), df['age'].idxmax(), alpha=0.75)
plt.suptitle('En genç ve en yaşlı milyarderler', color='r')
plt.ylabel('y ekseni')
plt.xlabel('x ekseni')
plt.grid()
plt.show()
# endregion


# region  hangi ayda doğan milyarderlerin sayısı en fazla
df['birthDate'] = pd.to_datetime(df['birthDate'])
df['birthMonth'] = df['birthDate'].dt.month
df['birthMonth'].value_counts().sort_values(ascending=False)
df['birthMonth'].value_counts().idxmax()
# endregion


# region Veri setindeki milyarderlerin yaşları ile servetleri arasında bir ilişki var mı yoksa bu iki özellik arasında herhangi bir ilişki görüyor musunuz?
df['age']
df['finalWorth']

plt.figure(figsize=(10, 7))
plt.scatter(df['age'], df['finalWorth'], color='blue', alpha=0.5)
plt.title('Milyarderlerin Yaş ve Servet İlişkisi')
plt.xlabel('Yaş')
plt.ylabel('Servet')
plt.grid()
plt.show()

corr = df['age'].corr(df['finalWorth'])  # kolerasyon katsayısı -1 ve 1 arasında olur. -1'e yaklaştıkça iki özellik arasındaki ilişki zayıflar.
print(f'Yaş ve Servet Arasındaki Korelasyon Katsayısı:', corr)
# endregion


# region kaç tane milyarderler selfmade kaç tanesi değil
df['selfMade'].value_counts()
# endregion


# region En fazla hangi source ile ilgilenildiğini bulup listele ve bar grafiğinde göster
df_source_sayisi = df['source'].value_counts().drop_duplicates()
df_source_sayisi.plot(kind='bar', stacked=False, alpha=0.75, figsize=(10,7))
plt.suptitle('Source Sayısı Bar Grafiği', color='r')
plt.ylabel('Y ekseni', color='r')
plt.xlabel('X ekseni', color='r')
plt.xticks(rotation=90)
plt.grid()
plt.show()
# endregion


# region Temizlediğin dosyayı yazdır
df.to_csv('Data/clean_forbes_2022')
# endregion