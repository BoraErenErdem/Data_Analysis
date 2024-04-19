

import pandas as pd
import numpy as np
from os import path

df = pd.read_csv("Data/youtube-ing.csv")
print(df)


# region en çok görüntülenmeye sahip ilk 10 farklı videonun title ve views sütunlarını ekrana bas
print(df.groupby('title')[['title', 'views']].sum(numeric_only = True).sort_values('views', ascending=False).head())  # sum() methodunu kullandık çünkü farklı kanallardan yüklenmiş olabilir. Sadece numeric_only= True dedik çünkü NaN olan sonuçları değil sadece sayı olan sonuçları istiyoruz.
# endregion


# region categorilerin idlerine göre likes ortalamasını bulun ilk 10 videoyu listele
print(df.groupby('category_id')[['likes']].mean(numeric_only=True).sort_values('likes', ascending=False).head(10))
# endregion


# region hangi kanal ne kadar yorum almış
print(df.groupby('channel_title')[['comment_count']].sum(numeric_only=True).sort_values('comment_count', ascending=False).head(10))
# endregion


# region her bir video için kullanılan tags sayısı için tag count isimli yeni bir sütun yaratalım. sonra da title ve tag count yazalım. (custom function yaz) (apply() kullan)

# 1.Yol
def tag_count(tags):
    return tags.count("|")

df['tag count'] = df['tags'].apply(tag_count)

print(df[['title', 'tag count']])


# 2.Yol
df['tag count'] = df['tags'].apply(lambda x: x.count("|"))  # lambda'daki x seçili sütunun her hücresine x diyip o hücreleri sayıyor.
print(df[['title', 'tag count']])
# endregion


# region Her bir video için kullanılan taglerin uzunluğunu hesaplayarak, yeni bir sütun oluşturun. Ardından, bu yeni sütunu ve video başlıklarını içeren bir DataFrame yazdır

# 1.Yol
def tag_sayici(tags):
    return tags.count("|")

df['tag sayısı'] = df['tags'].apply(tag_sayici)

print(df[['title', 'tag sayısı']].sort_values('tag sayısı', ascending=False))


# 2.Yol
df['tag sayısı'] = df['tags'].apply(lambda x: x.count('|'))
print(df[['title', 'tag sayısı']])
# endregion


# region Her bir description için içindeki kelime sayısını hesaplayarak yeni bir sütun oluşturun.

# 1.Yol
def description_kelime_sayisi(description):  # Bu custom fonksiyonda descriptionun string olması halinde kelimelerini sayıp toplaması için fonksiyon yazdık
    if isinstance(description, str):  # isinstance() methodu eğer description string bir ifade ise kelimeleri sayıp toplasın diye komut verdik
        return sum(len(i) for i in description.split(" "))
    else:
        return 0


df['description_kelime_sayisi'] = df['description'].apply(description_kelime_sayisi)
print(df[['title', 'description_kelime_sayisi']])


# 2.Yol
df['description_kelime_sayisi'] = df['description'].apply(lambda x: sum(len(i) for i in x.split(" ")) if isinstance(x, str) else 0)
print(df[['title', 'description_kelime_sayisi']])
# endregion


# region her bir videonun like ve dislike oranlarını bulalım. like_avg isimli yeni bir sütun yazalım. yazacağımız function argüman olarak veri setini alcak ve bu sütunu kullanarak sorgu yaz
def like_dislike_ortalamasi(data_set: pd.DataFrame):
    like_listesi = list(data_set['likes'])
    dislike_listesi = list(data_set['dislikes'])

    birlesmis_liste = list(zip(like_listesi, dislike_listesi))
    ortalama_listesi = []

    for like, dislike in birlesmis_liste:
        if like + dislike == 0:
            ortalama_listesi.append(0)
        else:
            ortalama_listesi.append(like / (like + dislike))
    return ortalama_listesi


df['like_avg'] = like_dislike_ortalamasi(df)


print(df.sort_values('like_avg', ascending=False)[['title', 'likes', 'dislikes', 'like_avg']].to_string())
# endregion


# region Hangi kategorideki videoların toplam izlenme sayısı en yüksektir
print(df.groupby(['category_id', 'title'])[['views']].sum(numeric_only=True).sort_values('views', ascending=False).head(1))
# endregion


# region Videoların yayın tarihlerine göre izlenme sayısının zaman içindeki değişimi nasıldır?
print(df.groupby(['title', 'publish_time'])[['views']].sum().sort_values('views', ascending=False))
# endregion


# region Kanal başına ortalama izlenme sayısı nedir ve en çok views olan kanal hangisidir?  # ????? viewsi sıralayınca izlenme sayıları doğru sıralanmıyor ?????
print(df.groupby('channel_title')[['views']].mean(numeric_only=True).sort_values('views', ascending=False))
# endregion


# region Videoların title uzunluklarını hesapla ve yeni sütun oluştur.

# 1.Yol
df['title_lenght'] = df['title'].apply(lambda x: len(x))
print(df[['title_lenght']].sort_values('title_lenght', ascending=False))

# 2.Yol
def title_uzunlugu_hesaplama(title):
    return len(title)

df['title uzunluğu'] = df['title'].apply(title_uzunlugu_hesaplama)
print(df[['title uzunluğu']].sort_values('title uzunluğu', ascending=False))
# endregion


# region En çok hangi videoların başlıklarında en çok tags kullanılmıştır ve aynı sayıda tag kullananları gösterme.
df['title_tags'] = df['title'].apply(lambda x: x.count("|"))
print(df[['title_tags']].sort_values('title_tags', ascending=False).drop_duplicates())
# endregion


# region Hangi kanalların videoları daha fazla beğeni ve daha az beğeniyi alıyor bunu bul ve yeni sütun oluşturup ilk 10'u listele

# 1.Yol
print(df.query('likes > dislikes')[['channel_title', 'likes', 'dislikes']].sort_values('likes', ascending=False))

# 2.Yol
df['like_dislike_avg'] = df['likes'] - df['dislikes']
print(df[['title','like_dislike_avg']].sort_values('like_dislike_avg', ascending=False).head(10))
# endregion


# region Her bir kanalın toplam izlenme sayısını hesaplayarak en fazla izlenen ilk 10 kanalı sıralayın.
print(df.groupby('channel_title')[['views']].sum(numeric_only=True).sort_values('views', ascending=False).head(10))
# endregion


# region Her bir kanalın videolarının ortalama beğeni oranını hesaplayarak en yüksek ortalama beğeni oranına sahip ilk 5 kanalı bulun.
df['like_dislike_diff'] = df['likes'] - df['dislikes']
sonuc = df.groupby('channel_title')[['like_dislike_diff']].sum() / df['channel_title'].count()
print(sonuc.sort_values('like_dislike_diff', ascending=False).head())
# endregion


# region Hangi kanalın videoları en çok yorum alıyor?
print(df.groupby('channel_title')[['comment_count']].sum(numeric_only=True).sort_values('comment_count', ascending=False).head(1))
# endregion


# region Hangi kanalın videoları toplamda en çok izlenme sayısına sahiptir?
print(df.groupby('channel_title')[['views']].sum(numeric_only=True).sort_values('views', ascending=False).head(1))
# endregion


# region Hangi kanalın videoları, ortalama olarak en yüksek like/dislike oranına sahiptir?  # ?????? kontrol ettir ?????
df['like dislike oranı'] = df['likes'] / (df['likes'] + df['dislikes'])

print(df.groupby('channel_title')[['like dislike oranı']].sum().sort_values('like dislike oranı', ascending=False))
# endregion


# region Hangi kanalın videoları ortalama olarak en yüksek izlenme sayısına sahip   # ????????? çıktıda hata var ?????????
print(df.groupby('channel_title')[['views']].mean().sort_values('views', ascending=False))


df['ortalama izlenme sayısı'] = (df['views'].sum()) / (df['channel_title'].count())

print(df.groupby('channel_title')[['ortalama izlenme sayısı']].max().sort_values('ortalama izlenme sayısı', ascending=False))  # ikisi farklı sonuç veriyor
print(df.groupby('channel_title')[['ortalama izlenme sayısı']].idxmax().sort_values('ortalama izlenme sayısı', ascending=False))
# endregion




# region Hangi kanalın videoları, ortalama olarak en yüksek beğeni sayısına sahiptir?  # ????? çıktıda hata var ??????
print(df.groupby('channel_title')[['views']].mean().sort_values('views', ascending=False).head(1))
# endregion


# region Hangi kanalın videoları ortalama olarak en fazla yorum alıyor?
print(df.groupby('channel_title')[['comment_count']].mean().sort_values('comment_count', ascending=False).head(1))
# endregion


# region Hangi 2 kanalın videolarının ortalama olarak en fazla yorum sayısına sahip olduğunu bul
print(df.groupby('channel_title')[['comment_count']].mean().sort_values('comment_count', ascending=False).head(2))
# endregion


# region title içinde 'new' kelimesi geçen en yüksek views'e sahip videoyu yazdır

# 1.Yol
def string_bulucu(title: str):
    if 'new' in title.lower():
        return True
    else:
        return False

print(df[df['title'].apply(string_bulucu)][['title', 'views']].sort_values('views', ascending=False).head(1))

# 2.Yol
print(df[df['title'].apply(lambda x: 'new' in x.lower())][['title', 'views']].sort_values('views', ascending=False))
# endregion


# region trending_date'sı en yeni olan videoyu göster
print(df[['trending_date', 'title']].sort_values('trending_date',ascending=False).head(1))
# endregion


# region ilk 10 kaydı getir
print(df.head(10))
# endregion


# region ikinci 5 kaydı getiriniz
print(df[5:10])
# endregion


# region data'da bulunan sütun isimleri ve sayısını bul
print(df.columns)  # sütunların isimlerini bulma
print(df.columns.shape[0])  # sütunların sayısını bulma
print(df.shape[1])  # sütunların sayısını bulma
# endregion


# region likes ve dislikes sayılarının ortalaması
print(df['likes'].mean())
print(df['dislikes'].mean())
# endregion


# region ilk 50 videonun likes ve dislikes sütunları
print(df[['likes', 'dislikes', 'title']].head(50))
# endregion


# region en çok görüntülenen video hangisi
print(df.groupby('title')[['views']].max().sort_values('views', ascending=False).head(1))
# endregion


# region en düşük görüntülenen video hangisidir
print(df.groupby('title')[['views']].idxmin().sort_values('views', ascending=False).tail(1))
# endregion


# region en fazla görüntülenen ilk 10 video
print(df.sort_values('views', ascending=False)[['title', 'views']].head(10))
# endregion


# region Kategoriye göre beğeni ortalamalarını sıralı şekilde getir
print(df.groupby('category_id')[['likes']].mean().sort_values('likes', ascending=False))
# endregion


# region kategoriye göre yorum sayılarını sıralı şekilde getir
print(df.groupby('category_id')[['comment_count']].sum().sort_values('comment_count', ascending=False))
# endregion


# region her kategoride kaç video var
print(df.groupby('category_id')[['title']].count().sort_values('title', ascending=False))
# endregion


# region Her videonun title uzunluğu bilgisini yeni sütunda göster

# 1.Yol
df['title_uzunlugu'] = df['title'].apply(lambda x: x.count(""))
print(df[['title_uzunlugu']].sort_values('title_uzunlugu', ascending=False))

# 2.Yol
def title_uzunlugu(title):
    return len(title)

df['title_uzunlugu'] = df['title'].apply(title_uzunlugu)
print(df[['title_uzunlugu']].sort_values('title_uzunlugu', ascending=False))
# endregion


# region her video için kullanılan tags sayısını yeni sütunda göster

# 1.Yol
def tags_calculator(tags):
    if '|' in tags:
        return tags.count("|")
    else:
        return 0

df['tags calculator'] = df['tags'].apply(tags_calculator)
print(df[['tags calculator', 'title']].sort_values('tags calculator', ascending=False))

# 2.Yol
df['tags calculator'] = df['tags'].apply(lambda x: x.count("|"))
print(df[['tags calculator', 'title']].sort_values('tags calculator', ascending=False))
# endregion


# region En popüler videoları like/dislike oranına göre listele
def like_dislike_ortalamasi(df: pd.DataFrame):
    likelistesi = list(df['likes'])
    dislikelistesi = list(df['dislikes'])

    birlesikliste = list(zip(likelistesi,dislikelistesi))
    ortalamalistesi = []
    for like, dislike in birlesikliste:
        if like + dislike == 0:
            ortalamalistesi.append(0)
        else:
            ortalamalistesi.append(like / (like + dislike))
    return ortalamalistesi

df['like_dislike_orani'] = like_dislike_ortalamasi(df)
print(df[['title', 'like_dislike_orani']].sort_values('like_dislike_orani', ascending=False))
# endregion


# region thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description sütunlarını silip kalan sütunları göster
newdf = df.drop(['thumbnail_link','comments_disabled','ratings_disabled','video_error_or_removed','description'], axis=1)
print(newdf)
# endregion