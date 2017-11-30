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
if "pg-headline" in CNN_headline:
    start_index = CNN_headline.find("pg-headline")
    CNN_headline = CNN_headline[start_index :- 1]
if "\"pg-headline\"" in CNN_headline:
    start_index = CNN_headline.find("\"pg-headline\"")
    CNN_headline = CNN_headline[start_index :- 1]
if "> "in CNN_headline:
    start_index = CNN_headline.find(">")
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
"""
print(nyt_S_addy)
print(huff_S_addy)
print(fox_S_addy)
#print(CNN_front_page)
print(CNN_S_addy)
"""
print("""<!DOCTYPE html>
<h1> NEWS </h1>
<img src=\"./photos/news.jpg\" >
<br>
<p1> <a href=\" """ + CNN_S_addy + """\">CNN </a> </p1>
<br>
<p1> Headline: """ + CNN_Headline + """
<br>
<p2><a href=\" """ + fox_S_addy + """ \"> FOX </a> </p2>
<br>
<p3><a href=\" """ + huff_S_addy + """ \"> HUFFINGTON POST </a> </p3>
<br>
<p4> <a href=\" """ + nyt_S_addy +""" \"> NEW YORK TIMES </a> </p4>
""")
