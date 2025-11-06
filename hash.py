import hashlib

texto = "ayuda"
hash_hex = hashlib.sha3_512(texto.encode()).hexdigest()
print("SHA-256:", hash_hex)