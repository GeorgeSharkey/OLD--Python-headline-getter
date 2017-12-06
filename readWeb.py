import urllib
#reads from CNN.com
CNN_link = "https://www.cnn.com"
f = urllib.urlopen(CNN_link)
CNN_front_page = f.read()
#looks for top story
if "Top" in CNN_front_page:
    start_index = CNN_front_page.find("Top")
    CNN_front_page = CNN_front_page[start_index:-1]
if "uri" in CNN_front_page:
    start_index = CNN_front_page.find("uri")
    CNN_front_page = CNN_front_page[start_index:-1]
if "\"/" in CNN_front_page:
    start_index = CNN_front_page.find("\"/")
    CNN_front_page = CNN_front_page[start_index+1:-1]
CNN_S_addy = "https://www.cnn.com"
#gets the actual link to the current top story from cnn
for i in CNN_front_page:
    if i == "\"":
        break
    else:
        CNN_S_addy = CNN_S_addy + i

#now it does everything again but with the new link to get the headline:
CNN_link = CNN_S_addy
f = urllib.urlopen(CNN_link)
CNN_headline = f.read()
#looks for headline
if "title" in CNN_headline:
    start_index = CNN_headline.find("title")
    CNN_headline = CNN_headline[start_index :- 1]
if ">" in CNN_headline:
    start_index = CNN_headline.find(">")
    CNN_headline = CNN_headline[start_index :- 1]
if "-"in CNN_headline:
    start_index = CNN_headline.find("-")
    CNN_headline = CNN_headline[start_index +1 :- 1]

# loop to get just the headline;removes everthing off the end
CNN_Headline = ""
for i in CNN_headline:
    if i == "<":
        break
    else:
        CNN_Headline = CNN_Headline + i

#fox
fox_link = "https://www.foxnews.com"
f = urllib.urlopen(fox_link)
fox_front_page = f.read()
#looks for top story
if "article story" in fox_front_page:
    start_index = fox_front_page.find("article story")
    fox_front_page = fox_front_page[start_index:-1]

if "f=\"" in fox_front_page:
    start_index = fox_front_page.find("f=\"")
    fox_front_page = fox_front_page[start_index+3:-1]

fox_S_addy = ""
#gets the actual link to the current top story from fox
for i in fox_front_page:
    if i == "\"":
        break
    else:
        fox_S_addy = fox_S_addy + i

#For headline
fox_link = fox_S_addy
f = urllib.urlopen(fox_link)
fox_Headline = f.read()

if "\"title\"" in fox_Headline:
    start_index = fox_Headline.find("\"title\"")
    fox_Headline = fox_Headline[start_index:-1]

if ":" in fox_Headline:
    start_index = fox_Headline.find(":")
    fox_Headline = fox_Headline[start_index +3 :-1]
fox_headline=""
for i in fox_Headline:
    if i == "\"":
        break
    else:
        fox_headline = fox_headline + i


#Huffingtonpost
huff_link = "https://www.huffingtonpost.com"
f = urllib.urlopen(huff_link)
huff_front_page = f.read()
#looks for top story
if "card__splash__wrapper js-" in huff_front_page:
    start_index = huff_front_page.find("card__splash__wrapper js-")
    huff_front_page = huff_front_page[start_index:-1]

if "f=\"" in huff_front_page:
    start_index = huff_front_page.find("f=\"")
    huff_front_page = huff_front_page[start_index+3:-1]

huff_S_addy = "https://www.huffingtonpost.com/"
#gets the actual link to the current top story from huff
for i in huff_front_page:
    if i == "\"":
        break
    else:
        huff_S_addy = huff_S_addy + i
#for headline
#huffingtonpost likes to throw 403 errors so we use huff_front_page to limit http requests


if "-title__" in huff_front_page:
    start_index = huff_front_page.find("-title__")
    huff_front_page = huff_front_page[start_index:-1]


if ">" in huff_front_page:
    start_index = huff_front_page.find(">")
    huff_front_page = huff_front_page[start_index + 1:-1]

huff_Headline = ""


for i in huff_front_page:
    if i == "<":
        break
    else:
        huff_Headline = huff_Headline + i


#New York Times
nyt_link = "https://www.nytimes.com/"
f = urllib.urlopen(nyt_link)
nyt_front_page = f.read()
#looks for top story
if "story-heading\">" in nyt_front_page:
    start_index = nyt_front_page.find("story-heading\">")
    nyt_front_page = nyt_front_page[start_index:-1]

if "f=\"" in nyt_front_page:
    start_index = nyt_front_page.find("f=\"")
    nyt_front_page = nyt_front_page[start_index+3:-1]

nyt_S_addy = ""
#gets the actual link to the current top story from nyt
for i in nyt_front_page:
    if i == "\"":
        break
    else:
        nyt_S_addy = nyt_S_addy + i

f = urllib.urlopen(nyt_S_addy)
nyt_headline = f.read()
#gets headline

if "title" in nyt_headline:
    start_index = nyt_headline.find("title")
    nyt_headline = nyt_headline[start_index:-1]
if ">" in nyt_headline:
    start_index = nyt_headline.find(">")
    nyt_headline = nyt_headline[start_index + 1:-1]

nyt_Headline = ""
for i in nyt_headline:
    if i == "-":
        break
    else:
        nyt_Headline = nyt_Headline + i

print("""<!DOCTYPE html>
<br>
<link rel="stylesheet" href="./CSS/default.css">
<h1> NEWS </h1>
<br>
<p1> CNN: </p1>
<br>
<p1> <a href=\" """ + CNN_S_addy + """\"> Headline: """ + CNN_Headline + """ </a> </p1>
<br>
<br>
<p2> Fox: </p2>
<br>
<p2><a href=\" """ + fox_S_addy + """ \"> Headline: """ + fox_headline + """ </a> </p2>
<br>
<br>
<p3> HUFFINGTON POST: </p3>
<br>
<p3><a href=\" """ + huff_S_addy + """ \"> Headline: """ + huff_Headline + """ </a> </p3>
<br>
<br>
<p4> NEW YORK TIMES </p4>
<br>
<p4> <a href=\" """ + nyt_S_addy +""" \"> Headline: """ + nyt_Headline+ """ </a> </p4>
</body>
""")
