def get_num_words(text):
	words = text.split()
	return len(words)
def get_char_count(text):
    char_count = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char in char_count:
            char_count[lowered_char] += 1
        else:
            char_count[lowered_char] = 1
    return char_count
def sort_on(items):
    return items['count']
def sorted_char_count_dict(char_count):
    char_count_dict = []
    for char in char_count:
        char_count_dict.append(
            {'char': char, 'count': char_count[char]}
        )
    char_count_dict.sort(reverse=True, key=sort_on)
    return char_count_dict
