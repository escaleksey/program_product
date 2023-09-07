import os
from data.CONFIG import LANGUAGE_PATH
from json import load

def get_list_languages():
    files = os.listdir(LANGUAGE_PATH)
    languages = list(map(lambda x: x.replace('.json', ''), files))
    languages.remove('last_lang.txt')
    return languages

def get_names_of_languages():
    names_of_languages = []
    for item in get_list_languages():
        with open(f"static/lang/{item}.json", "r", encoding='UTF-8') as file:
            lang_dict = load(file)
        names_of_languages.append(lang_dict.get("name"))
    return names_of_languages






