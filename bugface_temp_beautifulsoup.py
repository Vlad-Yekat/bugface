def get_random_head_from_bloomberg():
    """
    before run you must install beautifulsoup in subfolder bs4
    """
    import urllib.request, urllib.parse, urllib.error
    from bs4 import BeautifulSoup
    import ssl
    import random

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = 'https://www.bloomberg.com'
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('h1')
    max_len = len(tags)
    rand_theme = random.randint(0,(max_len-1))
    #for i in range(max_len):
    i = rand_theme
    str_tag = str(tags[i])
    res_arr = str_tag.split(">")
    str_tag2 = res_arr[-3]
    res_arr2 = str_tag2.split("<")
    res_str = res_arr2[0].strip()

    return res_str

print(get_random_head_from_bloomberg())



