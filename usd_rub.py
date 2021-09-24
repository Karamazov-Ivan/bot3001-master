import requests
from bs4 import BeautifulSoup

TNG_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D1%82%D0%B5%D0%BD%D0%B3%D0%B5&newwindow=1&ei=gCkMYdK9I8ygjgaz-pmwDQ&oq=%D0%BA%D1%83%D1%80%D1%81+%D1%82%D0%B5%D0%BD%D0%B3%D0%B5&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyCAgAEIAEEIsDMggIABCABBCLAzIICAAQgAQQiwMyCAgAEIAEEIsDOgcIABBHELADOgcIABCwAxBDOgQIABBDOgUIABCRAjoJCAAQgAQQChAqOgcIABCABBAKOgoIABCABBAKEIsDOgUILhCABDoRCC4QgAQQiwMQqAMQmAMQmgM6DgguEIAEEIsDEKgDEJ0DSgQIQRgAUNycSFi3u0hg1rxIaARwAngAgAHCAogBmg2SAQc2LjcuMC4xmAEAoAEBsAEAyAEKuAEDwAEB&sclient=gws-wiz-serp&ved=0ahUKEwjS_ZiivZryAhVMkMMKHTN9BtYQ4dUDCA0&uact=5'

EUR_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&newwindow=1&ei=miIMYbO0O4H8rgTiqq6wDw&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyCAgAEIAEEIsDMggIABCABBCLAzIICAAQgAQQiwMyCAgAEIAEEIsDOgcIABBHELADOgcIABCABBAKSgQIQRgAUMmsDlj5sw5gurkOaAJwAngAgAGfA4gBigqSAQkwLjEuMy4wLjGYAQCgAQHIAQi4AQPAAQE&sclient=gws-wiz-serp&ved=0ahUKEwiz6aTYtpryAhUBvosKHWKVC_YQ4dUDCA0&uact=5'

USD_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&source=hp&ei=JA4MYZ6zCJKXlwSrurKoBQ&iflsig=AINFCbYAAAAAYQwcNGLxuWoqIr1NLAtC7C5j0xPANYAw&oq=%D0%BA%D1%83%D1%80%D1%81&gs_lcp=Cgdnd3Mtd2l6EAMYADIKCAAQgAQQRhCCAjIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoICC4QgAQQkwI6CwguEIAEEMcBENEDOgsILhCABBDHARCjAjoFCC4QgAQ6DgguEIAEEMcBENEDEJMCUIYIWIEZYOIeaANwAHgAgAGSAYgBjgWSAQMzLjOYAQCgAQGwAQA&sclient=gws-wiz'

headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0'}



def usd():

    full_page = requests.get(USD_RUB, headers=headers)

    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class":"DFlfde SwHCTb"})


    return convert[0].text
    
def eur():

    full_page = requests.get(EUR_RUB, headers=headers)

    soup = BeautifulSoup(full_page.content, 'html.parser')
    
    convert = soup.findAll("span", {"class":"DFlfde SwHCTb"})

    return convert[0].text

def tng():

    full_page = requests.get(TNG_RUB, headers=headers)

    soup = BeautifulSoup(full_page.content, 'html.parser')
    
    convert = soup.findAll("span", {"class":"DFlfde SwHCTb"})

    return convert[0].text




        

