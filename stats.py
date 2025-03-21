from collections import defaultdict

def get_num_words(text):
    return len(text.split())


def get_num_char(text):
    default = defaultdict(int)
    for char in text:
        char = char.lower()
        if char == ' ':
            continue
        else:
            default[char] += 1
    return sorted(default.items(), key=lambda x: x[1], reverse=True)