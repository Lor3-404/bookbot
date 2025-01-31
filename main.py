def word_count(file_contents):
    return len(file_contents.split())
    

def count_strings(file_contents):
    character_count = {}
    lowered_string = file_contents.lower()
    for letter in lowered_string:
        if letter.isalpha():
            if letter in character_count:
                character_count[letter] += 1
            else:
                character_count[letter] = 1
    return character_count


def display_count(character_count):
    for key in (character_count):
        print(f"The '{key}' character was found {character_count[key]} times")


def main():
    file_contents = ""

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
           
    words = word_count(file_contents)
    character_count = count_strings(file_contents)    
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    display_count(character_count)

main()