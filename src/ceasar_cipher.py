alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def find_letter(cur_letter, shift):
    cur_index = alphabet.index(cur_letter)
    new_index = (cur_index + shift) % len(alphabet)
    return alphabet[new_index]

def cipher(word, shift):
    ciphered_word = ""
    for c in word:
        ciphered_word += find_letter(c, shift)
    return ciphered_word

def decipher(word, shift):
    deciphered_word = ""
    for c in word:
        deciphered_word += find_letter(c, -shift)
    return deciphered_word

def interface():
    word_to_cipher = input("Give me a word: ").lower()
    shift = int(input("Tell me the desired shift: "))
    ciphered_word = cipher(word_to_cipher, shift)
    print(f"Your word was ciphered as: {ciphered_word}.")
    print()
    word_to_decipher = input("Give me a word to decipher: ").lower()
    shift = int(input("Tell me the shift: "))
    deciphered_word = decipher(word_to_decipher, shift)
    print(f"Your word was deciphered as: {deciphered_word}.")

if __name__ == "__main__":
    interface()