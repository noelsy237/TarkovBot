import json

output = []

with open('raw-price-html.txt', encoding='utf-8') as f:
    lines = f.readlines()

    count = 0
    dict = {}
    for line in lines:
        if count == 0:
            dict = {'href': line}
            count += 1
        elif count == 1:
            dict['title'] = line
            output.append(dict)
            count = 0

with open('price.json', 'w') as f:
    json.dump(output, f)