with open("static/lang/last_lang.txt", "r") as f:
    LANGUAGE_JSON = f.read()


def get_lang():
    return LANGUAGE_JSON.strip()


LAST_LANGUAGE = get_lang()
