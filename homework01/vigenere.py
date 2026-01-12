def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword = keyword.upper()
    keyword_length = len(keyword)
    
    for i, char in enumerate(plaintext):
        if char.isalpha():
            if char.isupper():
                alphabet_start = ord('A')
                key_char = keyword[i % keyword_length]
                shift = ord(key_char) - ord('A')
                
                shifted_char = chr((ord(char) - alphabet_start + shift) % 26 + alphabet_start)
                ciphertext += shifted_char
            else:
                alphabet_start = ord('a')
                key_char = keyword[i % keyword_length].upper()
                shift = ord(key_char) - ord('A')
                
                shifted_char = chr((ord(char) - alphabet_start + shift) % 26 + alphabet_start)
                ciphertext += shifted_char
        else:
            ciphertext += char
    
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword = keyword.upper()
    keyword_length = len(keyword)
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            if char.isupper():
                alphabet_start = ord('A')
                key_char = keyword[i % keyword_length]
                shift = ord(key_char) - ord('A')
                
                shifted_char = chr((ord(char) - alphabet_start - shift) % 26 + alphabet_start)
                plaintext += shifted_char
            else:
                alphabet_start = ord('a')
                key_char = keyword[i % keyword_length].upper()
                shift = ord(key_char) - ord('A')
                
                shifted_char = chr((ord(char) - alphabet_start - shift) % 26 + alphabet_start)
                plaintext += shifted_char
        else:
            plaintext += char
    
    return plaintext
