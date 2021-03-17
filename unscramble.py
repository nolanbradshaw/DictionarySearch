import json

def unscramble_word(search_str, data, index):
    # Creating a copy to iterate over.
    data_copy = data.copy()
    
    if index >= len(search_str):
        # Check that the sorted versions of each word match.
        for key in data_copy:
            if sorted(search_str) != sorted(key):
                del data[key]
        return data
    
    # Remove all words that don't contain the same letters or length.
    for key in data_copy:
        if search_str[index] not in key or len(key) != len(search_str):
            del data[key]

    index += 1
    return unscramble_word(search_str, data, index)

with open('dictionary_compact.json') as dict_file:
    data = json.load(dict_file)

    search_str = input('Enter the word/letters you want to use: ')
    print(list(unscramble_word(search_str, data, 0).keys()))