import json

def get_lang_codes(lang_code):
    with open ('locale.json') as f:
        data = json.load(f)

    langs = data[lang_code]
    return [
        '{lang}_{terr}'.format(lang=lang_code, terr=terr)
        for terr in langs
    ]

print(__file__)
print(get_lang_codes('pl'))
