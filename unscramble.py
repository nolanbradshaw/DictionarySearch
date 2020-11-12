import json 

def unscrambleWord(search_str, key_arr, index):
    if index >= len(search_str):
        for i in key_arr:
            if sorted(search_str) != sorted(key_arr[i]):
                key_arr.remove(i)
        return key_arr

    # Don't want to manipulate the array
    # we are iterating over.
    key_copy = key_arr.copy()

    for j in key_copy:
        if search_str[index] not in j or len(j) != len(search_str):
            key_arr.remove(j)

    # If nothing has been removed from the array.
    if key_copy == key_arr:
        for i in key_arr:
            if sorted(search_str) != sorted(i):
                key_arr.remove(i)
        return key_arr

    index += 1
    return unscrambleWord(search_str, key_arr, index)

with open('dictionary_compact.json') as dict_file:
    data = json.load(dict_file)
    keys = list(data.keys())

    operation_str = input('Enter the word/letters you want to use: ')

    print(unscrambleWord(operation_str, keys, 0))