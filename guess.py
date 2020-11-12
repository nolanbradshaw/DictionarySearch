import json 

keys = []

def searchDict(search_str):
    output = keys.copy()
    for k in range(0, len(search_str)):
        current = search_str[k]
        for j in keys:
            if current not in j:
                if j not in output:
                    continue
                output.remove(j)

    return output

with open('dictionary_compact.json') as dict_file:
    data = json.load(dict_file)
    keys = list(data.keys())

    search_str = input('Enter the letters you want to search by: ')
    print(searchDict(search_str))

