

import pandas as pd
import numpy as np
from os import path

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


# region En taşlı ilk 2 kullanıcıyı isimlerine göre listele
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