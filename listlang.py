import lxml.etree
import json

path = 'supplementalData.xml'

with open (path) as f:
    langxml = bytes(f.read(), 'utf-8')
langtree = lxml.etree.XML(langxml)

langs = {}
territories = None
for t in langtree.find('languageData').findall('language'):
    if t.get('territories') is not None and t.get('scripts') == 'Latn':
        territories = t.get('territories').split(' ')
    langs[t.get('type')] = territories

with open ('locale.json', 'w') as f:
    json.dump(langs, f)
