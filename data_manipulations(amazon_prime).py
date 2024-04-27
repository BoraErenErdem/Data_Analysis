

import pandas as pd
import numpy as np
from os import path
import matplotlib.pyplot as plt

df = pd.read_csv('Data/amazon_prime_users.csv')
print(df.to_string())


# region ilk 5 ve son 5 satırı göster
print(df)
# endregion


# region Gender Female olanları listele
print(df[df['Gender'] == 'Female'][['Name', 'Username']].sort_values('Name', ascending=False))
# endregion


# region Feedback/Ratings'i en yüksek olan kullanıcılardan birinin Name ve Email Address bilgilerini bul

# 1.Yol
print(df.groupby(['Name', 'Email Address'])[['Feedback/Ratings']].max().sort_values('Feedback/Ratings', ascending=False).head(1))  # bütün kullanıcıları puanına göre sıralar..!

# 2.Yol
print(df[df['Feedback/Ratings'] == df['Feedback/Ratings'].max()][['Name', 'Email Address', 'Feedback/Ratings']].sort_values('Feedback/Ratings', ascending=False).to_string())  # Sadece maksimum puana sahip kullanıcıalrı verir..!
# endregion


# region Feedback/Ratings'i en düşük olan kullanıcılardan birinin Name ve Email Address bilgilerini bul

# 1.Yol
print(df[df['Feedback/Ratings'] == df['Feedback/Ratings'].min()][['Name', 'Email Address', 'Feedback/Ratings']].sort_values('Feedback/Ratings', ascending=False).to_string())  # sadece minimum puana sahip kullanıcıları verir..!

# 2.Yol
print(df.groupby(['Name', 'Email Address'])[['Feedback/Ratings']].min().sort_values('Feedback/Ratings', ascending=False).tail(1))  # bütün kullanıcıları puanına göre sıralar..!
# endregion


# region Hangi kullanıcıların Membership Start Date süreci en önce başlamıştır

# 1.Yol
print(df.groupby('Name')[['Membership Start Date']].min().sort_values('Membership Start Date', ascending=False).to_string())  # bütün kullanıcıları tarihe göre sıralar..!

# 2.Yol
print(df[df['Membership Start Date'] == df['Membership Start Date'].min()][['Name', 'Membership Start Date']].sort_values('Membership Start Date', ascending=False))  # sadece en önce olan tarihe sahip kullanıcıları verir..!
# endregion


# region Favorite Genres içinde Drama ve Documentary olanları listele ve bu kişilerin sayısını bul
def drama_ve_documentary_bulucu(Favorite_Genres):
    if 'Drama' and 'Documentary' in Favorite_Genres:
        return True
    else:
        return False


result = df[df['Favorite Genres'].apply(drama_ve_documentary_bulucu)][['Name', 'Gender']].sort_values('Name', ascending=False)
print(result.to_string())
print(result.shape[0])
# endregion


# region En yaşlı 2 kullanıcıyı isimlerine göre listele
print(df.groupby('Name')[['Date of Birth']].max().sort_values('Date of Birth', ascending=False).tail(2))
# endregion


# region Kaç farklı Subscription Plan vardır
print(df.groupby('Subscription Plan').count().drop_duplicates())
# endregion


# region Kullanıcıların yaşadıkları yerleri listele
print(df['Location'].to_string())
# endregion


# region Hangi 2 kullanıcıın Customer Support Interactions fazladır
print(df.groupby(['Name', 'Customer Support Interactions']).max().sort_values('Customer Support Interactions', ascending=False).head(2))
# endregion


# region Payment Information Visa olanların Name, Email Address, Membership Start Date, Membership End Date listele
print(df[df['Payment Information'] == 'Visa'][['Name', 'Email Address', 'Membership End Date', 'Payment Information']].sort_values('Membership End Date', ascending=False).to_string())
# endregion


# region Hangi tür kullanıcılar en çok video izleme süresine sahiptir ve hangi cihazları kullanıyorlar (Devices Used) (Usage Frequency)
print(df[df['Usage Frequency'] == df['Usage Frequency'].max()][['Name', 'Gender','Usage Frequency', 'Devices Used']].sort_values('Usage Frequency', ascending=False))
# endregion


# region Hangi kullanıcıların Username içinde 'x', 's', 'z', '0' yer almaktadır.
def username_bulucu(Username: str):
    if 'x' in Username.lower() and 's' in Username.lower() and 'z' in Username.lower():
        return True
    else:
        return False


print(df[df['Username'].apply(username_bulucu)][['Username', 'Name']].sort_values('Username', ascending=False).to_string())
# endregion


# region Amazon Prime kullanıcılarının yaş dağılımını göstermek için bir histogram oluştur  ???? xticks S O R ?????
df['Date of Birth'] = pd.to_datetime(df['Date of Birth'])  # pd.to_datetime() fonksiyonu 'Date of Birth' sütunundaki değerleri datetime nesnelerine dönüştürdü ve işlem yapmamız kolaylaştı
df['Age'] = pd.Timestamp.now().year - df['Date of Birth'].dt.year  # pd.Timestamp.now().year ifadesi şu anki yılın değerini verir. Bu değeri kullanıcıların doğum yıllarının değerlerinden çıkartarak yaşlarını hesaplıyoruz. dt.year ifadesi datetime nesnesinin yıl kısmını döndürür.
print(df[['Name','Age']])

count, bin_edges = np.histogram(df['Age'], bins=10)
print(count)
print(bin_edges)

df['Age'].plot(kind='hist', figsize=(10,7), stacked=False, alpha=0.5, color='blue', xticks=bin_edges)
plt.suptitle('Amazon Prime kullanıcılarının yaş dağılımını gösteren histogram grafiği', color='r')
plt.ylabel('Kullanıcı Sayısı', color='r')
plt.xlabel('Yaş', color='r')
plt.grid()
plt.show()
# endregion


# region Cinsiyete göre Prime kullanıcılarının sayısını göstermek için bir bar plot oluştur
df_gender_sayici = df['Gender'].value_counts()
print(df_gender_sayici)

df_gender_sayici.plot(kind='bar', stacked=False, figsize=(10,7), alpha=0.75, color='green')
plt.title('Cinsiyete Göre Prime Kullanıcılarının Sayısının Bar Grafiği', color='r')
plt.ylabel('Cinsiyetlere Göre Kullanıcı Sayısı', color='r')
plt.xlabel('Cinsiyet', color='r')
plt.show()
# endregion


# region Prime üyeliğine katılan kullanıcıların üyelik planları ne kadar ve planları cinsiyete göre bar grafiği çiz
df_plan = df.groupby('Subscription Plan')[['Subscription Plan', 'Gender']].value_counts()
print(df_plan)

df_plan.plot(kind='bar', figsize=(10,7), stacked=False, alpha=0.50, color='b')
plt.title('Cinsiyete göre üyelik dağılımı', color='r')
plt.ylabel('Üyelik Sayısı', color='r')
plt.xlabel('Cinsiyet', color='r')
plt.grid()
plt.show()
# endregion


# region Prime üyeliğine katılan kullanıcıların üyelik planları ne kadar ve planları cinsiyete göre pasta grafiği çiz ve yüzde dilimlerini pastanın içinde göster
df_plan = df.groupby('Subscription Plan')[['Subscription Plan', 'Gender']].value_counts()
print(df_plan)

df_plan.plot(kind='pie', figsize=(10,7), shadow=True, labels=None, stacked=False, autopct='%1.1f%%', startangle=90, pctdistance=0.5, explode=[0.1,0.1,0.1,0.1])
plt.axis('equal')
plt.title('Cinsiyete göre üyelik dağılımı pasta grafiği', color='r')
plt.legend(labels=df_plan.index, prop={'size':8})
plt.show()
# endregion


# region Prime üyeliğine katılan kullanıcıların cinsiyet dağılımını pasta grafiği ile göster
df_cinsiyet = df['Gender'].value_counts()
print(df_cinsiyet)

df_cinsiyet.plot(kind='pie', stacked=False, figsize=(10,7), autopct='%1.1f%%', pctdistance=1.1, shadow=True, labels=None, explode=[0.1,0.1], startangle=90)
plt.axis('equal')
plt.suptitle('Kullanıcıların Cinsiyetine Göre Pasta Grafiği', color='r', size=15)
plt.legend(labels=df_cinsiyet.index, prop={'size':10})
plt.show()
# endregion


# region Prime üyeliğine katılan kullanıcıların hangi ülkelerden olduğu ve bu ülkelerdeki Prime kullanıcı sayılarını histogram ile göster
df_ulke_dagilimi = df.groupby('Location')[['Location']].value_counts()
print(df_ulke_dagilimi.to_string())

count, bin_edges = np.histogram(df_ulke_dagilimi, bins=10)
print(count)
print(bin_edges)
df_ulke_dagilimi.plot(kind='hist', stacked=False, alpha=0.50, xticks=bin_edges, color='b', figsize=(10,7))
plt.suptitle('ülkelerdeki Prime kullanıcı sayılarını histogram grafiği', color='r', size=12)
plt.ylabel('Kullanıcı Sayısı', color='r')
plt.xlabel('Ülkeler', color='r')
plt.grid()
plt.show()
# endregion


# region Prime üyeliğine katılan kullanıcıların üyelik süreleri ne kadar? Bu sürelerde bir artış veya azalış var mı bunu çizgi grafiği ile göster.
df['Membership Start Date'] = pd.to_datetime(df['Membership Start Date'])
df['Membership End Date'] = pd.to_datetime(df['Membership End Date'])

df['üyelik süreci'] = df['Membership End Date'] - df['Membership Start Date']
print(df['üyelik süreci'])


df['üyelik süreci'].plot(kind='line', linestyle='-.' ,stacked=False, alpha=0.50, figsize=(10,7))
plt.suptitle('Prime Video Üyelik Süreci Pasta Grafiği', color='black', size=12)
plt.ylabel('Kullanıcı Sayısı', color='r')
plt.xlabel('Günler', color='r')
plt.legend(labels=df['üyelik süreci'], prop={'size': 10})
plt.grid()
plt.show()
# endregion


# region Prime üyeliğine katılan kullanıcılar arasında en çok tercih edilen kategori nelerdir? Bunu pasta grafiği ile göster
df_category = df['Favorite Genres'].value_counts()
print(df_category)

df_category.plot(kind='pie', stacked=False, figsize=(10,7), pctdistance=1.1, autopct='%1.1f%%', explode=[0.1,0.1,0.1,0.1,0.1,0.1,0.1], shadow=True, labels=None, startangle=90)
plt.axis('equal')
plt.suptitle('Prime üyeliğine katılan kullanıcılar arasında en çok tercih edilen kategorler pasta grafiği'.upper(), color='black')
plt.legend(df_category.index, prop={'size':10})
plt.show()
# endregion


# region Amazon Prime kullanıcılarının hangi ayda üyeliklerini başlattığını gösteren bir histogram grafik oluştur
df['Membership Start Date'] = pd.to_datetime(df['Membership Start Date'])
df['Kalan Üyelik Süresi'] = pd.Timestamp.now().month - df['Membership Start Date'].dt.month
print(df[['Membership Start Date','Kalan Üyelik Süresi']])

count, bin_edges = np.histogram(df['Kalan Üyelik Süresi'], bins=15)
print(count)
print(bin_edges)


df['Kalan Üyelik Süresi'].plot(kind='hist', figsize=(10,7), stacked=False, alpha=0.50, color='green', xticks=bin_edges)
plt.title('Prime Kullanıcılarının Kalan Üyelik SÜresi', color='r')
plt.ylabel('Kullanıcı Sayısı', color='r')
plt.xlabel('Üyelik Süresi', color='r')
plt.legend(labels=df['Kalan Üyelik Süresi'].index, prop={'size': 8})
plt.grid()
plt.show()
# endregion


# region Amazon Prime Video kullanıcılarının hangi cihazları kullandığını gösteren bir pasta grafiği oluştur
df_device_count = df['Devices Used'].value_counts()
df_device_count.plot(kind='pie', stacked=False, figsize=(10,7), autopct='%1.1f%%', pctdistance=1.1, explode=[0.1, 0.1, 0.1], shadow=True, labels=None, startangle=90)
plt.axis('equal')
plt.suptitle('Amazon Prime Video kullanıcılarının hangi cihazları kullandığını gösteren pasta grafiği'.upper(), size=12, color='r')
plt.legend(df_device_count.index, prop={'size': 10})
plt.show()
# endregion


# region Amazon Prime Video kullanıcılarının hangi tür içerikleri en çok izlediğini göstermek için bir çubuk grafik oluştur
df_tercihler = df['Favorite Genres'].value_counts()
print(df_tercihler)

df_tercihler.plot(kind='bar', figsize=(10,7), stacked=False, alpha=0.50, color=['red', 'cyan', 'green', 'purple', 'orange', 'yellow', 'blue'])
plt.title('Amazon Prime Video kullanıcılarının tercih ettiği türler', size=12, color='r')
plt.ylabel('Tercih Sayısı', color='r')
plt.xlabel('Türler', color='r')
plt.grid()
plt.show()
# endregion


# region Hangi ülkeler Amazon Prime Video kullanıcılarının en çok olduğu ülkelerdir? İlk 10 ülkeyi bilgiyi bir çubuk grafiği kullanarak göster
country_counts = df['Location'].value_counts().head(10)

country_counts.plot(kind='bar', figsize=(10, 7), color='yellowgreen', stacked=False)
plt.title('Amazon Prime Video Kullanıcılarının En Çok Olduğu Ülkeler')
plt.xlabel('Ülke')
plt.ylabel('Kullanıcı Sayısı')
plt.xticks(rotation=45)
plt.show()
# endregion


# region Hangi şehirlerde Amazon Prime Video kullanıcıları daha aktiftir ilk 10'u bar grafiği halinde göster
df.sort_values('Usage Frequency', ascending=False, inplace=True)
df_frecequency = df.groupby('Usage Frequency')[['Location']].value_counts().head(10)
print(df_frecequency.head(10))


df_frequent.head(10).plot(kind='bar', figsize=(10,7), stacked=False)
plt.suptitle('Şehirlerdeki Amazon Prime Video Kullanıcıları Aktiflik Grafiği', size=15, color='r')
plt.ylabel('Aktiflik sayısı', color='r')
plt.xlabel('Lokasyon', color='r')
plt.xticks(rotation=45)
plt.show()
# endregion


# region Amazon Prime Video kullanıcılarının abonelik sürelerini gün olarak bul ve bar grafiğinde göster.
df['Membership Start Date'] = pd.to_datetime(df['Membership Start Date'])
df['Subscription Duration'] = pd.Timestamp.now() - df['Membership Start Date']
df['Subscription Duration'] = df['Subscription Duration'].dt.days
df['Subscription Duration'].plot(kind='hist',bins=20, color='skyblue', edgecolor='black', figsize=(10,7))
plt.title('Amazon Prime Video Kullanıcılarının Abonelik Süreleri Dağılımı')
plt.xlabel('Abonelik Süresi (Gün)')
plt.ylabel('Kullanıcı Sayısı')
plt.grid()
plt.show()
# endregion