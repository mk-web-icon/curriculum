#1章-章末課題
#問題①
#問1-1.下の画像のように、それぞれを2乗した値を出力できるよう以下のfor文を完成させて下さい。
#--------------------------
data = [1,3,5,7]
for i in data:
  print(i**2)


#問1-2.range()を使って問1-1と同じ結果が表示されるようなfor文を完成させて下さい。
#--------------------------
for j in range(1,8,2):
  print(j**2)


#問題②
#問2-1.下の画像のような出力になるように、コードを完成させてください。
#--------------------------
all_place = ["札幌","東京","横浜","大阪","名古屋","福岡"]
wait_place = ["札幌","大阪"]
get_place = ["横浜"]

for place in all_place:
  if place in get_place:
    print(place + "のチケットが当選しました！")
  elif place in wait_place:
    print(place + "のチケットは結果待ち")
  else:
    print(place + "のチケットは落選しました")

#問2-2.下の画像のような出力になるように、問2-1の続きにコードに追加してください。
#--------------------------
all_place = ["札幌","東京","横浜","大阪","名古屋","福岡"]
get_place = ["横浜","札幌","大阪"]

for place in all_place:
  if place in get_place:
    print(place + "のチケットが当選しました！")
  elif place in wait_place:
    print(place + "のチケットは結果待ち")
  else:
    print(place + "のチケットは落選しました")

print("{}のチケットが当選しました！".format("と".join(get_place)))