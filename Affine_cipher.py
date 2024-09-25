m = 256
a = 43
b = 51

# find the inverse element a modulo m using the extended Euclidean algorithm
def gcd_extended(a, m):
    if a == 0:
        return m, 0, 1
    gcd, x1, y1 = gcd_extended(m % a, a)
    x = y1 - (m // a) * x1
    y = x1
    return gcd, x, y

# find the inverse element to a modulo m
def mod_inverse(a, m):
    gcd, x, y = gcd_extended(a, m)
    if gcd != 1:
        raise ValueError("a and m are not mutually simple, there is no inverse element")
    else:
        return x % m

def affine_encrypt_bytes(data, a, b, m):
    encrypted_data = bytearray()
    for byte in data:
        encrypted_byte = (a * byte + b) % m
        encrypted_data.append(encrypted_byte)
    return encrypted_data

def affine_decrypt_bytes(data, a, b, m):
    decrypted_data = bytearray()
    a_inv = mod_inverse(a, m)
    decrypted_text = []
    for byte in data:
        decrypted_byte = (a_inv * (byte - b)) % m
        decrypted_data.append(decrypted_byte)
    return decrypted_data

def process_file(input_file, encrypted_file, decrypted_file, a, b, m):
    with open(input_file, 'rb') as file:
        original_data = file.read()
    
    encrypted_data = affine_encrypt_bytes(original_data, a, b, m)
    with open(encrypted_file, 'wb') as file:
        file.write(encrypted_data)
    
    decrypted_data = affine_decrypt_bytes(encrypted_data, a, b, m)
    with open(decrypted_file, 'wb') as file:
        file.write(decrypted_data)

input_file = 'input.jpg'
encrypted_file = 'encrypted.jpg'
decrypted_file = 'decrypted.jpg'
print("The file has been successfully encrypted and decrypted")

process_file(input_file, encrypted_file, decrypted_file, a, b, m)
