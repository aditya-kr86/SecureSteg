# xor.py

def xor_encrypt(message: str, key: str) -> str:
    encrypted = ''
    for i in range(len(message)):
        encrypted += chr(ord(message[i]) ^ ord(key[i % len(key)]))
    return encrypted

def xor_decrypt(encrypted: str, key: str) -> str:
    decrypted = ''
    for i in range(len(encrypted)):
        decrypted += chr(ord(encrypted[i]) ^ ord(key[i % len(key)]))
    return decrypted
