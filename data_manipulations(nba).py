

import numpy as np
import pandas as pd
from os import path
import matplotlib.pyplot as plt

# print(path.abspath("nba.csv"))


# region En yüksek maaşı alan oyuncu kim

# 1.Yol
df = pd.read_csv("Data/nba.csv")
max_salary = (df['Salary'].max())
max_salary_name = df[df['Salary'] == max_salary][['Name','Salary']]
print(max_salary_name)
print(max_salary)

# 2.Yol
print(df[df['Salary'] == df['Salary'].max()][['Name', 'Salary']])
# endregion


# region Takımlara göre oyuncuların maaş ortalaması nedir
print(df.groupby("Team")[['Salary']].mean().sort_values("Salary"))
# endregion


# region veri setinde kaç farklı takım var
print(df['Team'].nunique())  # .nunique() methodu null olan sayıları almayacağı için groupby methodundan daha doğru çıktı verir. o yüzden burada nunique() kullandık.
# endregion


# region yaşı 20 ile 35 arasında olan oyuncuların adı, takımı, yaş bilgilerini ve yaş bilgisine göre çoktan aza sıralayacak şekilde ekrana basın

# 1.Yol
df = pd.read_csv("Data/nba.csv")
print(df.query(" 20 <= Age <= 35")[['Name', 'Team', 'Age']].sort_values("Age", ascending=False).to_string())

# 2.Yol
print(df[df['Age'].between(20,35)][['Name', 'Team', 'Age']].sort_values("Age", ascending=False).to_string())
# endregion


# region ismi içerisinde 'and' ifadesi geçen oyuncuları listeleyen bir custom function yazın ve bu fonksiyonu dataframe uygula
def string_bul(name):
    if 'and' in name.lower():
        return True
    else:
        return False


print(df[df['Name'].apply(string_bul)])
# endregion


# region takım adı içerisinde 'tic' ifadesi geçen takımın oyuncularını listeleyen bir custom function yazın ve bu fonksiyonu dataframe uygula
def takim_bulucu(Team: str):
    if 'tic' in Team.lower():
        return True
    else:
        return False


print(df[df["Team"].apply(takim_bulucu)][['Name']])
# endregion


# region College adı içerisinde 'a', 's', 't' harfleri olan oyuncuların isimlerini sırala

# NOT: isinstance() methodunu kullandık çünkü verinin College kısmında bütün yazılanlar metin yani string olması gerekirken bazı yerlerde float tipinde yazılmışi Hata almamak veya hatayı önlemek için isinstance() methodunu kullandık...!

def harf_bulucu(college: str):
    if isinstance(college, str) and 'a' in college.lower() and 's' in college.lower() and 't' in college.lower():
        return True
    else:
        return False


print(df[df['College'].apply(harf_bulucu)][['Name', 'College']].sort_values("Name", ascending=False).to_string())
# endregion


# region "Boston Celtics" takımındaki oyuncuların yaş ortalamasını hesapla

print(df[df['Team'] == "Boston Celtics"][["Age"]].mean())
# endregion


# region Brooklyn Nets takımındaki oyuncuların kilo ortalamasını hesaplayın
print(df[df["Team"] == "Brooklyn Nets"][["Weight"]].mean())
# endregion


# region Hangi takımda kaç oyuncu bulunmakta
print(df.groupby("Team")[["Name"]].count())
# endregion


# region Hangi takımda en genç oyuncu kimdir?
print(df.groupby("Team")[["Name", "Age"]].min().sort_values("Age", ascending=False))
# endregion


# region Hangi takımda en yaşlı oyuncu kimdir?
print(df.groupby("Team")[['Name', 'Age']].max().sort_values("Age"))
# endregion


# region Her takımda kaç farklı pozisyonda oyuncu bulunmaktadır?
df.groupby("Team")[["Position"]].nunique()  # Her takımda aynı pozisyon sayısını saymasın farklı pozisyonları saysın diye nunique() kullandık.
# endregion


# region En çok maaş alan oyuncu kimdir ve ne kadar maaş almaktadır

# 1.Yol
print(df.groupby("Salary")[["Name", "Salary"]].max().tail(1))

# 2.Yol
print(df[df['Salary'] == df['Salary'].max()][['Name', 'Salary']])
# endregion


# region Hangi takım en düşük maaş ortalamasına sahiptir?
print(df.groupby("Team")[['Salary']].mean().min())  # en düşük maaş ortalaması fiyatı
print(df.groupby("Team")[['Salary']].mean().idxmin())  # en düşük maaş ortalaması olan takım
# endregion


# region Hangi takım en yüksek maaş ortalamasına sahiptir?
print(df.groupby("Team")[["Salary"]].mean().idxmax())  # en yüksek maaş ortalaması olan takım
print(df.groupby("Team")[["Salary"]].mean().max())  # en yüksek maaş ortalaması fiyatı
# endregion


# region Hangi takımda en fazla oyuncu bulunan üniversite/okul hangisidir? (College)
print(df.groupby("Team")[["College"]].count().idxmax())  # en fazla üniversite/okul oyuncusu bulunan takım.
# endregion


# region Hangi takım en yüksek ortalama oyuncu ağırlığına sahiptir?
print(df.groupby('Team')[['Weight']].mean().idxmax())
# endregion


# region En düşük yaş ortalamasına sahip takımın adı ve yaş ortalaması nedir?

# 1.Yol
print(df.groupby("Team")[['Age']].mean().sort_values("Age", ascending=False).tail(1))
# endregion


# region En yüksek maaşı alan oyuncunun takımdaki pozisyonu nedir
print(df.groupby('Position')[['Salary', 'Name']].max().sort_values('Salary',ascending=False))  # rastgele max maaşa sahip oyunculardan birini veriyor

print(df[df['Salary'] == df.groupby('Position')['Salary'].transform('max')])  # doğru olan çözüm
# endregion


# region ilk 10 kaydı getir
df = pd.read_csv('Data/nba.csv')
print(df.to_string())

print(df.head(10))
# endregion


# region toplam kayıt miktarı ne kadardır
print(df.shape[0])
# endregion


# region tüm oyuncuların toplam maaş ortalaması
print(df['Salary'].mean())
# endregion


# region En yüksek oyuncunun maaşı ne kadardır

# 1.Yol
print(df.groupby('Salary')[['Name']].max().sort_values('Salary', ascending=False).head(1))

# 2.Yol
print(df[df['Salary'] == df['Salary'].max()][['Name', 'Salary']])
# endregion


# region Yaşları 20 ile 25 arasında olan oyuncuların ismini ve oynadıkları takımları azalan şekilde sıralı olarak getir

# 1.Yol
print(df.query('20 <= Age <= 25')[['Name', 'Team', 'Age']].sort_values('Age', ascending=False).to_string())

# 2.Yol
print(df[df['Age'].between(20, 25)][['Name', 'Team', 'Age']].sort_values('Age', ascending=False).to_string())  # between() fonksiyonu ile == operatörü kullanılmaz çünkü == verdiğimiz zaman serinin her bir değerini belirli bir ararlığa karşı karşılaştıramadığımız için Empty DataFrame elde ettmiş oluruz. Yani between() fonksiyonu ile == kullanılmaz.

# 3.Yol
print(df[(df['Age'] >= 20) & (df['Age'] <= 25)][['Name', 'Team', 'Age']].sort_values('Age', ascending=False).to_string())
# endregion


# region "John Holland" isimli oyuncunun oynadığı takım hangisidir ve aldığı maaş nedir
def oyuncu_bulucu(Name):
    if Name == 'John Holland':
        return True
    else:
        return False

print(df[df['Name'].apply(oyuncu_bulucu)][['Team', 'Name', 'Salary']])

# 2.Yol
print(df[df['Name'] == 'John Holland'][['Team', 'Salary']])
# endregion


# region Takımlara göre oyuncuların ortalama maaş bilgisi
print(df.groupby('Team')[['Salary']].mean()[['Salary']].sort_values('Salary', ascending=False).to_string())
# endregion


# region kaç farklı takım var
print(df['Team'].nunique())
# endregion


# region Her takımda kaç oyuncu oynamaktadır
print(df.groupby('Team')[['Name']].count())
# endregion


# region ismi içinde 'cur' geçen kayıtları bul

# 1.Yol
def isim_bulucu(Name):
    if 'cur' in Name.lower():
        return True
    else:
        return False

print(df[df['Name'].apply(isim_bulucu)].to_string())

# 2.Yol
print(df[df['Name'].apply(lambda x: 'cur' in x.lower())].to_string())
# endregion


# region Takımların ortalama maaşlarını gösteren bir çizgi grafiği yapın (ilk 5 takımı gösterin)
df.groupby('Team')[['Salary']].mean().head().plot(kind='bar', figsize=(10,7), stacked=False, alpha=0.50)
plt.title('NBA Takımlarının Maaş Ortalamalarının Bar Grafiği', color='r')
plt.ylabel('Takım Sayısı', color='r')
plt.xlabel('Takımlar', color='r')
plt.legend()
plt.show()
# endregion


# region Oyuncuların yaş dağılımını gösteren bir histogram oluştur
df_sorted = df.sort_values('Age', ascending=False)[['Name', 'Age']]
print(df_sorted)

df_age = df_sorted['Age']
print(df_age)

count, bin_edges = np.histogram(df_age, bins=10)
print(count)
print(bin_edges)

df_age.plot(kind='hist', figsize=(10,7), stacked=False, alpha=0.50, color='green')
plt.title('Yaşlarına göre histogram grafiği', color='r')
plt.ylabel('Oyuncu Sayısı', color='r')
plt.xlabel('Yaş', color='r')
plt.grid()
plt.show()
# endregion


# region Takımların oyuncu sayısını gösteren bir çubuk grafik oluştur
df_player_count = df.groupby('Team')[['Team']].count()
print(df_player_count)

df_player_count.plot(kind='bar', stacked=False, figsize=(10,7), alpha=0.50, color='b')
plt.title('Takımlara göre oyuncu sayısı bar grafiği', color='r')
plt.ylabel('Takım Sayısı', color='r')
plt.xlabel('Oyuncu Sayısı', color='r')
plt.grid()
plt.show()
# endregion


# region Oyuncuların pozisyon dağılımını gösteren bir pasta grafiği oluştur
df_pozisyon_dagilimi = df.groupby('Position')[['Position']].count()
print(df_pozisyon_dagilimi)

df_pozisyon_dagilimi['Position'].plot(kind='pie', stacked=False, shadow=True, labels=None, startangle=90, figsize=(10,7), autopct='%1.1f%%', pctdistance=1.1, explode=[0.1, 0.1, 0.1, 0.1, 0.1])
plt.axis('equal')
plt.title('Oyuncuların Pozisyon Dağılımını Gösteren Pasta Grafiği')
plt.legend(labels=df_pozisyon_dagilimi.index)
plt.show()
# endregion


# region Takımların oyuncularının ortalama yaşlarının dağılımını göstermek için bir histogram oluştur
df_takimlarin_ort_yasi = df.groupby('Team')[['Age']].mean()
print(df_takimlarin_ort_yasi.sort_values('Age', ascending=False))

count, bin_edges = np.histogram(df_takimlarin_ort_yasi, bins=10)
print(count)
print(bin_edges)

df_takimlarin_ort_yasi.plot(kind='hist', stacked=False, alpha=0.50, figsize=(10,7), color='purple', bins=10)
plt.title('Takımlara göre oyuncuların ortalama yaşlarının histogram grafiği', color='black')
plt.ylabel('Takım Sayısı', color='black')
plt.xlabel('Ortalama Yaş', color='black')
plt.grid()
plt.show()
# endregion


# region Veri setindeki oyuncuların takımlarına göre ortalama yaşlarının kutu grafiği (box plot) ile dağılımını göster
df_takimlarin_ort_yasi = df.groupby('Team')[['Age']].mean()
print(df_takimlarin_ort_yasi.sort_values('Age', ascending=False))

df_takimlarin_ort_yasi.plot(kind='box', figsize=(10,7), stacked=False, color='b', vert=False)
plt.title('Takımalra Göre Oyuncuların Ortalama Yaşlarının Kutu Grafiği', color='black')
plt.ylabel('Takımlar', color='black')
plt.xlabel('Ortalama Yaş',color='black')
plt.grid()
plt.show()
# endregion


# region Veri setindeki oyuncuların takımlarına göre ortalama yaşlarını göstermek için bir çubuk grafik oluştur
df_takimlarin_ort_yasi = df.groupby('Team')[['Age']].mean()
print(df_takimlarin_ort_yasi.sort_values('Age', ascending=False))

df_takimlarin_ort_yasi.plot(kind='bar', figsize=(10,7), stacked=False, alpha=0.50, color='r')
plt.title('Takımlara göre oyuncuların ortalama yaşlarının bar grafiği', color='black')
plt.ylabel('Takım Sayısı', color='black')
plt.xlabel('Ortalama Yaş', color='black')
plt.show()
# endregion


# region Veri setindeki oyuncuların yaş ve pozisyon dağılımını göstermek için bir scatter plot oluştur
df_oyuncu_yas = df['Age']
print(df_oyuncu_yas)
df_oyuncu_pozisyon = df['Position']
print(df_oyuncu_pozisyon)
plt.figure(figsize=(10,7))  # figsize parametresini doğru şekilde kullanmak için plt.figure() fonksiyonu içinde tanımlayıp yaz yoksa aşağıdaki kullanımla çakışıyor
plt.plot(df_oyuncu_yas, df_oyuncu_pozisyon, 'o', alpha=0.50, color='blue')  # 'o' sembolüyle scatter plot oluşturulur
plt.title('Oyuncuların Yaş ve Pozisyon Dağılımı', color='black')  # birden fazla dataframe kullanıp hepsini plt.plot() yazıp içine önce x ekseni sonra y ekseni halinde yazdık
plt.ylabel('Pozisyon', color='b')
plt.xlabel('Yaş', color='b')
plt.grid()
plt.show()
# endregion