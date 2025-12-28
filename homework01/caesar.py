def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                start = ord('A')
                new_pos = (ord(char) - start + shift) % 26
                ciphertext += chr(start + new_pos)
            else:
                start = ord('a')
                new_pos = (ord(char) - start + shift) % 26
                ciphertext += chr(start + new_pos)
        else:
            ciphertext += char
    
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                start = ord('A')
                new_pos = (ord(char) - start - shift) % 26
                plaintext += chr(start + new_pos)
            else:
                start = ord('a')
                new_pos = (ord(char) - start - shift) % 26
                plaintext += chr(start + new_pos)
        else:
            plaintext += char
    
    return plaintext
