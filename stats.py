def count_words(text: str) -> int:
    return len(text.split())

def n_char(text: str) -> int:
    result = {}
    characters = []
    for char in text:
        characters.append(char.lower())

    unique_char = tuple(characters)
        
    print(characters)
    print(unique_char)

n_char("Hello this is python again")