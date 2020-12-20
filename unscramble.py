import json 

def unscrambleWord(search_str, key_arr, index):
    # Creating a copy to avoid manipulating an array
    # we are iterating over.
    key_copy = key_arr.copy()
    
    if index >= len(search_str):
        # Check that the sorted versions of each word match (this handles duplicate letters)
        [key_arr.remove(key) for key in key_copy if sorted(search_str) != sorted(key)]
        return key_arr
    
    [key_arr.remove(key) for key in key_copy if search_str[index] not in key or len(key) != len(search_str)]

    index += 1
    return unscrambleWord(search_str, key_arr, index)

with open('dictionary_compact.json') as dict_file:
    data = json.load(dict_file)
    keys = list(data.keys())

    search_str = input('Enter the word/letters you want to use: ')

    print(unscrambleWord(search_str, keys, 0))