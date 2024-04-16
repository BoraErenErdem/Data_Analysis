

import pandas as pd
from os import path

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