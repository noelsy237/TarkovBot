import json

priceLines = []
dataLines = []
count = 0

with open('tarkov-market.json') as f:
    priceLines = json.load(f)

with open('tarkov-tools.json', encoding="utf8") as f:
    dataLines = json.load(f)

for item in priceLines:
    for dataItem in dataLines:
        if item['aliases'][0] == dataItem['name'] or item['aliases'][0] in dataItem['aliases']:
            count += 1
            dataItem['href'] = item['href']
            count += 1
        else:
            dataItem['href'] = ""

with open('output.json', 'w') as f:
    json.dump(dataLines, f)

print(count)