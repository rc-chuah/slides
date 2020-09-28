import re

values = [
    '11',
    '٣', # arabic 3
    '½', # unicode 1/2
    '②', # unicode circled 2
    '߄', # NKO 4 (a writing system for the Manding languages of West Africa)
    '६', # Devanagari aka. Nagari (Indian)
    '_', # underscrore
    '-', # dash
    'a', # latin a
    'á', # Hungarian
    'א', # Hebrew aleph

]

for val in values:
    print(val)
    match = re.search(r'\w', val)
    if match:
        print('Match ', match.group(0))

