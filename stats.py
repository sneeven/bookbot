def count_words(text: str) -> int:
    return len(text.split())

def n_char(text: str) -> int:
    result = {}
    text = text.lower()

    for char in text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result 



#convert to lowercase , and count the unique characters (also the whitespace) -> add it to a dictonairy with {'p' : 6121} as key:value pair