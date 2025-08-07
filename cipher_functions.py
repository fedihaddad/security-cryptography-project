def caesar_cipher(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            # Convertir en majuscule pour le traitement
            char = char.upper()
            # Appliquer le décalage
            shifted = ord(char) - ord('A')
            shifted = (shifted + key) % 26
            result += chr(shifted + ord('A'))
        else:
            result += char
    return result

def caesar_decipher(text, key):
    return caesar_cipher(text, -key)

def affine_cipher(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():
            # Convertir en majuscule pour le traitement
            char = char.upper()
            # Appliquer la transformation affine
            x = ord(char) - ord('A')
            y = (a * x + b) % 26
            result += chr(y + ord('A'))
        else:
            result += char
    return result

def affine_decipher(text, a, b):
    # Trouver l'inverse modulaire de a
    a_inv = 0
    for i in range(26):
        if (a * i) % 26 == 1:
            a_inv = i
            break
    
    result = ""
    for char in text:
        if char.isalpha():
            # Convertir en majuscule pour le traitement
            char = char.upper()
            # Appliquer la transformation affine inverse
            y = ord(char) - ord('A')
            x = (a_inv * (y - b)) % 26
            result += chr(x + ord('A'))
        else:
            result += char
    return result

def letter_frequency(text):
    """Calcule la fréquence des lettres dans un texte"""
    freq = {}
    total = 0
    for char in text.upper():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
            total += 1
    
    # Convertir en pourcentages
    for char in freq:
        freq[char] = (freq[char] / total) * 100
    return freq

def brute_force_caesar(ciphertext):
    """Tente de déchiffrer un texte chiffré avec César en essayant toutes les clés possibles"""
    results = []
    for key in range(26):
        decrypted = caesar_decipher(ciphertext, key)
        results.append((key, decrypted))
    return results 