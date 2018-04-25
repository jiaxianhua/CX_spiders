import requests
import re
import time

def get_movie(n):
    n = int(n)
    for n in range (1, n):
        url = 'http://www.dytt8.net/html/gndy/dyzz/list_23_'+str(n)+'.html'
        html = requests.get(url)
        html.encoding = 'gb2312'
        movie_link = re.findall('<a href="/html/gndy/dyzz/(.*?)" class="ulink">', html.text)
        for movie_url in movie_link:
            movie_url = 'http://www.dytt8.net/html/gndy/dyzz/'+str(movie_url)
            movie_html = requests.get(movie_url)
            time.sleep(2)
            movie_html.encoding = 'gb2312'
            movie_name = re.findall('<div class="title_all"><h1><font color=#07519a>(.*?)</font></h1></div>' ,movie_html.text)
            movie_download_url = re.findall('<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(.*?)">' ,movie_html.text )
            print(movie_name)
            with open('movie.txt', 'a', encoding='utf-8') as ff:
                ff.write(movie_download_url[0] + '\n')

if __name__ == '__main__':
    page_name = input('请输入页数(<170):')
    get_movie(page_name)
