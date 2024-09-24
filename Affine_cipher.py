m = 256
a = 43
b = 51

# Find the inverse element a modulo m using the extended Euclidean algorithm
def gcd_extended(a, m):
    if a == 0:
        return m, 0, 1
    gcd, x1, y1 = gcd_extended(m % a, a)
    x = y1 - (m // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, y = gcd_extended(a, m)
    if gcd != 1:
        raise ValueError("a and m are not mutually simple, there is no inverse element")
    else:
        return x % m

def affine_encrypt(text, a, b, m):
    encrypted_text = []
    for char in text:
        M = ord(char)  # get the symbol code
        C = (a * M + b) % m  # encrypting the symbol
        encrypted_text.append(chr(C))  # convert it back to a character
    return ''.join(encrypted_text)

def affine_decrypt(text, a, b, m):
    a_inv = mod_inverse(a, m)  # Find the inverse element to a modulo m
    decrypted_text = []
    for char in text:
        C = ord(char)  # get the code of the encrypted character
        M = (a_inv * (C - b)) % m  # decrypting the symbol
        decrypted_text.append(chr(M))
    return ''.join(decrypted_text)

def process_file(input_file, encrypted_file, decrypted_file, a, b, m):
    with open(input_file, 'r', encoding='utf-8') as file:
        original_text = file.read()
    
    encrypted_text = affine_encrypt(original_text, a, b, m)
    with open(encrypted_file, 'w', encoding='utf-8') as file:
        file.write(encrypted_text)
    
    decrypted_text = affine_decrypt(encrypted_text, a, b, m)
    with open(decrypted_file, 'w', encoding='utf-8') as file:
        file.write(decrypted_text)

input_file = 'input.txt'
encrypted_file = 'encrypted.txt'
decrypted_file = 'decrypted.txt'

process_file(input_file, encrypted_file, decrypted_file, a, b, m)
