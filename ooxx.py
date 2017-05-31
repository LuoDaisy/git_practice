import urllib.request
import os

def get_number(url):
    html = open_url(url).decode('utf-8')
    #a = html.find('current-comment-page') + 23
    #b = html.find(']',a)
    #print(html[a:b])
    #return html[a:b]
    r = r'<span class="current-comment-page">\[([1-9]\d*)\]</span>'
    number = re.findall(r,html)
    print(number)
    return number[0]

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')

    responce = urllib.request.urlopen(req)
    html = responce.read()
    return html

def find_imgs(url):
    html = open_url(url).decode('utf-8')
    img_addrs = []

    a = html.find('img src=')

    while a != -1:
        b = html.find('.jpg', a, a + 255)
        if b != -1:
            img_addrs.append(html[a+11:b+4])
        else:
            b = a + 11
        a = html.find('img src=',b)
    return img_addrs

def save_imgs(folder,img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        url = 'http://' + each
        with open(filename,'wb') as f:
            img = open_url(url)
            f.write(img)

def download_mm(folder = '00xx',pages = 10):
    os.mkdir(folder)
    os.chdir(folder)

    url = 'http://jandan.net/ooxx/'
    page_number = int(get_number(url))

    for i in range(page_number):
        page_number -= 1
        page_url = url + 'page-' + str(page_number) +'#comments'

        img_addrs = find_imgs(page_url)
        save_imgs(folder,img_addrs)

if __name__ == '__main__':
    download_mm()
#为了实践git,增加的注释
