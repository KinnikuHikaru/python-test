import urllib.request, urllib.parse
params = {
    "name": "yoheim",
    "age": 29,
    "comment": "ああああ"
}
p = urllib.parse.urlencode(params)
url = "http://www.yoheim.net/?" + p
print(url)s
# => http://www.yoheim.net/?age=29&name=yoheim&comment=%E3%81%82%E3%81%82%E3%81%82%E3%81%82

with urllib.request.urlopen(url) as res:
   html = res.read().decode("utf-8")
   print(html)


# または簡単なパラメータの場合には、自分でつけちゃっても良い
url = "http://www.yoheim.net/blog.php?q=%d" % 20160203
print(url)
# => http://www.yoheim.net/blog.php?q=20160203