import requests
from bs4 import BeautifulSoup as bs
import random

def abc():
    return ["ПРИВЕТ", "ПОСТ", "ВРЕМЯ", "ПОКА"]


def _get_user_name_from_vk_id(user_id):
    request = requests.get("https://vk.com/id"+str(user_id))
    bs = bs4.BeautifulSoup(request.text, "html.parser")
    user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])
    return user_name.split()[0]

@staticmethod
def _clean_all_tag_from_str(string_line):

    """
    Очистка строки stringLine от тэгов и их содержимых
    :param string_line: Очищаемая строка
    :return: очищенная строка
    """

    result = ""
    not_skip = True
    for i in list(string_line):
        if not_skip:
            if i == "<":
                not_skip = False
            else:
                result += i
        else:
            if i == ">":
                not_skip = True

    return result

def parser_wall_text(domain):
    html = 'https://api.vk.com/method/wall.get?domain='+domain+'&access_token=fa15cdf7fa15cdf7fa15cdf7cefa64aeebffa15fa15cdf7a4b665149c53cc5bf287fba2&v=5.107'
    r = requests.get(html)
    json = r.json()
    text_post = []
    k = 0
    for i in range(len(json['response']['items'])):
        text_post.append(json['response']['items'][i]['text'])
        if len(text_post[i]) == 0:
            text_post[i] = 'Тут нет текста'
    return text_post

def parser_wall_img(domain):
    html = 'https://api.vk.com/method/wall.get?domain='+domain+'&access_token=fa15cdf7fa15cdf7fa15cdf7cefa64aeebffa15fa15cdf7a4b665149c53cc5bf287fba2&v=5.107'
    r = requests.get(html)
    json = r.json()
    img_post = []
    k = 0
    for i in range(len(json['response']['items'])):
        try:
            if len(json['response']['items'][i]['attachments']) == 1:
                max_size = len(json['response']['items'][i]['attachments'][0]['photo']['sizes']) - 1
                img_post.append(json['response']['items'][i]['attachments'][0]['photo']['sizes'][max_size]['url'])
            else:
                img_post.append([])
                k = len(img_post) - 1
                for j in range(len(json['response']['items'][i]['attachments'])):
                    max_size = len(json['response']['items'][i]['attachments'][j]['photo']['sizes']) - 1
                    img_post[k].append(json['response']['items'][i]['attachments'][j]['photo']['sizes'][max_size]['url'])
        except KeyError:
            img_post.append('https://static.tildacdn.com/tild3635-3033-4931-b636-333031333063/Logo5.jpg')
    return img_post
