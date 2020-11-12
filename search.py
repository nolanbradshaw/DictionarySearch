import json 

def searchDict(search_str, outputArr, index):

    if index >= len(search_str):
        return outputArr

    output_copy = outputArr.copy()

    for j in output_copy:
        if search_str[index] not in j:
            outputArr.remove(j)

    if output_copy == outputArr:
        return outputArr

    index += 1
    return searchDict(search_str, outputArr, index)

with open('dictionary_compact.json') as dict_file:
    data = json.load(dict_file)
    keys = list(data.keys())

    search_str = input('Enter the letters you want to search by: ')

    print(searchDict(search_str, keys, 0))

