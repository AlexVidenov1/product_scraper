import json

with open('product_data.json', 'r') as json_file:
    data = json.load(json_file)
    print(json.dumps(data, indent=4))
