import json

tkLines = []
ttLines = []
count = 0

with open('tarkov-market.json', encoding="utf8") as f:
    tkLines = json.load(f)

with open('tarkov-tools.json', encoding="utf8") as f:
    ttLines = json.load(f)

for ttItem in ttLines:
    for tkItem in tkLines:
        if ttItem['name'] == tkItem['name'] or ttItem['aliases'][0] == tkItem['name']:
            count += 1
            ttItem['href'] = tkItem['href']
            break
        else:
            ttItem['href'] = ""

with open('output.json', 'w') as f:
    json.dump(ttLines, f)

print(count)