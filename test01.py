urls = [
"http://www.google.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg",
"http://gliacloud.com/haha.png",
]

files = []
files2 = []
filesCount =[]

for url in urls:
    index = url.rindex("/")
    length: int = len(url)
    file = url[index+1:length]
    files.append(file)

files2 = list(set(files))

for file in files2:
    filesCount .append([file,files.count(file)])

def myFunc(e):
  return e[1]

filesCount.sort(key=myFunc, reverse=True)

for item in filesCount[:3]:
    print(item[0] + " " + str(item[1]))