import numpy as np

def teks_ke_angka(text):

    res = []
    for i in text.upper():
        if i.isalpha():
            res.append(ord(i) - 65)


    return res

def angka_ke_teks(nums):
    res = ''

    for i in nums:
        res += chr(int(round(i)) + 65)
    
    return res

def matriks_invers(matriks, mod=26):
    det = int(round(np.linalg.det(matriks)))

    det_inv = pow(det, -1, mod)

    matrix_mod_inv = (det_inv * np.round(det * np.linalg.inv(matriks)).astype(int)) % mod

    return matrix_mod_inv.astype(int)

def encrypt_hillcipher(plaintext, key):

    n = key.shape[0]
    P = teks_ke_angka(plaintext)
    
    while len(P) % n != 0:
        P.append(23)

    ciphertext = []
    for i in range(0, len(P), n):

        block = np.array(P[i:i+n])
        C = np.dot(key, block) % 26
        ciphertext.extend(C)

    return angka_ke_teks(ciphertext)

def decrypt_hillcipher(ciphertext, key):

    n = key.shape[0]
    C = teks_ke_angka(ciphertext)
    key_inv = matriks_invers(key, 26)

    plaintext = []
    for i in range(0, len(C), n):

        block = np.array(C[i:i+n])
        P = np.dot(key_inv, block) % 26
        plaintext.extend(P)

    return angka_ke_teks(plaintext)


key = np.array([[2, 1],
                [3, 4]])

plaintext = "KRIPTO"

ciphertext = encrypt_hillcipher(plaintext, key)
dekripsi = decrypt_hillcipher(ciphertext, key)


print("Ciphertext :", ciphertext)
print("Dekripsi   :", dekripsi)
