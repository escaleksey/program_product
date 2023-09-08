def get_lang():
    return LANGUAGE_JSON.strip()


with open("static/lang/last_lang.txt", "r") as f:
    LANGUAGE_JSON = f.read()

LAST_LANGUAGE = get_lang()
LANGUAGE_PATH = 'static/lang'

