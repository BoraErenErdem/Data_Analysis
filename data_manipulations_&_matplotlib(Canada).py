

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl  # openpyxl modülü xml dosyasını okunmasını sağlar


# region xlsx formatındaki excel'in 'Canada by Citizenship' isimli sheetini oku ve ilk 20 satır ve son 2 satır okuma.
df_can = pd.read_excel('Data/Canada.xlsx', sheet_name='Canada by Citizenship', skiprows=(20), skipfooter=2)  # skipfooter = sondan kaç satır atlamak istiyosan o kadarını gir
print(df_can.head().to_string())  # sheet_name = okumak istediğin sayfa ismini yaz
# endregion                       # skiprows = ilk kaç satırı atlamak istiyosan o kadarını gir


# region Eski sütun isimlerini yenileriyle değiştir (OdName ==> Country) (AreaName ==> Continent) (RegName ==> Region)
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
print(df_can.head().to_string())  # .rename(columns={}) bu fonksiyonda sütunların adını dictionarymiş gibi değiştirdik ve inplace=True ile üstüne kaydettik.
# endregion


# region AREA, REG, Type, Coverage, DevName sütunlarını sil
df_can.drop(['AREA','DEV' ,'REG', 'Type', 'Coverage', 'DevName'],axis=1, inplace=True)  # axis vermek zorudasın yoksa program satır mı sütun mu sileceğini bilemez
print(df_can.head().to_string())
# endregion


# region Sütun başlıklarının tiplerini ekrana bas
for i in df_can.columns:
    print(type(i))
# endregion


# region Sütun başlıklarının hepsinin tipini string yap
df_can.columns = list(map(str, df_can.columns))  # map() yinelenebilir bir objedeki (list, tuple) her bir öge için bir işlem uygular. Burada yenilenebilir obje df_can'in sütun başlıkları listesidir. Bu listedeki her bir itemin tipini string tipine map ettik.
for i in df_can.columns:
    print(type(i))
# endregion


# region df_can içerisinde var olan index yerine Country sütununu index olarak ayarla
df_can.set_index('Country', inplace=True)  # set_index() belirtilen bir sütunu indeks olarak ayarlar
print(df_can.head().to_string())                # reset_index() mevcut indeksi sıfırlar ve bir sıralı tamsayı indeksi ekler
# endregion                                     # set_axis() satır veya sütun indekslerini değiştirmek için kullanılır. Satır veya sütun indekslerini yeniden adlandırmayı sağlar.


# region Yıl yıl göçmen sayılarını toplayarak total isimli yeni sütuna yazdır
df_can['total'] = df_can.sum(numeric_only=True, axis=1)
print(df_can['total'])
# endregion


# region Veri setindeki yılları baz alarak kendimize benzer bir yıl listesi hazırlayalım lakin liste içerisindeki yıl bilgileri string olsun
years = list(map(str, range(1980, 2014)))
print(years)
# endregion


# region En çok göç vermiş 5 ülkeyi bul. df_top_five_country isimli df'e kaydet
df_can.sort_values('total', ascending=False, axis=0, inplace=True)
df_top_five_country = df_can.head()
print(df_top_five_country.head())
# endregion


# region Yukarıda oluşturulan df_top_five_country veri seti ile, year isimli listeyi kullanarak yılları satırlara ülkeleri sütunlara dönüştürerek bir df elde et bu df'i df_top_five_country üzerine ata
df_top_five_country = df_top_five_country[years].transpose()   # transpose() ile yıllar satır oldu Country'ler sütun oldu yani yer değiştirdi
print(df_top_five_country.head().to_string())
# endregion


# region Yukarıda oluşturulan df_top_five_country veri setinden faydalanarak alan grafiği yarat. plot() function kullanılarak yap.
df_top_five_country.plot(kind='area', stacked=False, figsize=(10,7), alpha=0.25)  # figsize() boyut
plt.title('En çok göç veren 5 ülke', color='r')                             # alpha() saydamlık
plt.ylabel(ylabel='Göçmen sayısı', color='r')                                     # stacked= yığılma olsun mu olmasın mı
plt.xlabel(xlabel='Yıllar', color='r')                                            # kind= tür
plt.show()
# endregion


# region Histogram grafiği yap. 2013 yılındaki göçmen hareketlerini histogram grafiğinde gösterelim. Grafiğin x düzlemindeki değerleri numpy kütüphanesinin histogram() fonksiyonuyla bul
count, bin_edges = np.histogram(df_can['2013'])
print(count)
print(bin_edges)

df_can['2013'].plot(kind='hist', stacked=False, figsize=(10,7), alpha=0.90, color='green', xticks=bin_edges)
plt.title('195 Ülkenin 2013 Yılındaki Göç Histogramı', c='r')
plt.ylabel(ylabel='Ülke sayısı', c='r')
plt.xlabel(xlabel='Göç sayısı', c='r')
plt.grid()  # grid() fonksiyonu daha rahat görelim diye araya ızgaralar ekler
plt.show()
# endregion


# region Baltık ülkelerinin verdiği göçmen sayısını histogram grafiğinde göster. Yıllar index ülkeler sütun olacak. Ülkeler Denmark, Norway, Sweden olsun. histogram() fonks. bins değeri ver.
df_baltic_countries = df_can.loc[['Denmark', 'Norway', 'Sweden'], years].transpose()
print(df_baltic_countries)

count, bin_edges = np.histogram(df_baltic_countries, bins=10)  # bins = grafikteki aralıkların sayısı
print(count)  # her bir bölümdeki değerlerin sayısını temsil eder
print(bin_edges)  # bölüm sınırlarını temsil eder

df_baltic_countries.plot(kind='hist', stacked=False, alpha=0.50, figsize=(10,7), color=['blue','purple','yellow'], xticks=bin_edges)  # xticks= ifadesi x ekseni için özelleştirilmiş işaret veya etiket ekler..!
plt.title('Denmark, Norway ve Sweden Histogram Grafiği (1980 - 2013)', color='green')
plt.ylabel(ylabel='Ülke Sayısı', color='green')
plt.xlabel(xlabel='Göç Sayısı', color='green')
plt.grid()
plt.show()
# endregion


# region 1980 - 2013 yılları arasında Iceland göçmenlerini histogram ile göster  ??????? bins ve xticks kullanım mantığını S O R ??????
df_iceland = df_can.loc['Iceland', years]
print(df_iceland)

count, bin_edges = np.histogram(df_iceland, bins=10)
print(count)
print(bin_edges)

df_iceland.plot(kind='hist', stacked=False, alpha=0.50, figsize=(10,7), color='r')
plt.title('Iceland Histogram Grafiği', color='orange')
plt.ylabel(ylabel='Ülke sayısı', color='r')
plt.xlabel(xlabel='Göç sayısı', color='r')
plt.grid()
plt.show()
# endregion


# region 1980 - 2013 yılları arasında Iceland göçmenlerini çubuk grafiği ile göster
df_iceland = df_can.loc['Iceland', years]
print(df_iceland)

df_iceland.plot(kind='bar', stacked=False, figsize=(10,7), alpha=0.50, color='r')
plt.title('iceland bar grafiği', color='r')
plt.ylabel(ylabel='Ülke sayısı', color='r')
plt.xlabel(xlabel='Göç Sayısı', color='r')
plt.grid()
plt.show()
# endregion


# region Kıtalara göre göçmen dağılımını pasta grafiğinde göster
df_continents = df_can.groupby('Continent').sum(numeric_only=True)
print(df_continents.head().to_string())

df_continents['total'].plot(kind='pie', stacked=False, figsize=(10,7), autopct='%1.1f%%', startangle=90, labels=None, shadow=True, pctdistance=1.1, explode=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
plt.axis('equal')  # pastanın dilimlerinin dairesel olmasını sağlar
plt.legend(labels=df_continents.index, prop={'size':8})  #  legend, grafiğin hangi renk veya stilin hangi veriyle ilişkilendirildiğini gösteren küçük bir açıklama kutusudur.
plt.show()  # labels, legendeki her bir öğenin etiketlerini içeren bir liste veya dizi olarak belirtilir. Bu etiketler genellikle grafiğin hangi veriyle ilişkilendirildiğini açıklar.
# autopct her bir dilime gelecek göçmen sayısını formatlayarak yazdırır
# startangle başlangıç açısıdır
# labels=None ülkelerin isimlerinin pasta dilimi üzerinde gözükmesini engeller
# explode, pastanın dilimlerini birbirinden uzaklaştırmak için kullanılır
# pctdistance, yüzde etiketlerinin her bir diliminin merkezden uzaklığını ayarlar
# endregion