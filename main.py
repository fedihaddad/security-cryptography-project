import sys
from cipher_functions import caesar_cipher, affine_cipher, caesar_decipher, affine_decipher

def get_valid_input(prompt, validation_func):
    while True:
        try:
            value = input(prompt)
            if validation_func(value):
                return value
            print("Valeur invalide. Veuillez réessayer.")
        except ValueError:
            print("Erreur de saisie. Veuillez réessayer.")

def validate_caesar_key(key):
    try:
        return 0 <= int(key) <= 25
    except ValueError:
        return False

def validate_affine_a(a):
    try:
        a = int(a)
        return a > 0 and a % 2 != 0 and a % 13 != 0
    except ValueError:
        return False

def validate_affine_b(b):
    try:
        return 0 <= int(b) <= 25
    except ValueError:
        return False

def main():
    print("=== Double Chiffrement César-Affine ===")
    print("1. Chiffrer un message")
    print("2. Déchiffrer un message")
    print("3. Quitter")
    
    choice = input("Votre choix (1-3): ")
    
    if choice == "1":
        message = input("Entrez le message à chiffrer: ")
        caesar_key = int(get_valid_input("Clé César (0-25): ", validate_caesar_key))
        affine_a = int(get_valid_input("Clé Affine a (premier avec 26): ", validate_affine_a))
        affine_b = int(get_valid_input("Clé Affine b (0-25): ", validate_affine_b))
        
        print("\nOrdre de chiffrement:")
        print("1. César puis Affine")
        print("2. Affine puis César")
        order = input("Votre choix (1-2): ")
        
        if order == "1":
            # César puis Affine
            temp = caesar_cipher(message, caesar_key)
            result = affine_cipher(temp, affine_a, affine_b)
        else:
            # Affine puis César
            temp = affine_cipher(message, affine_a, affine_b)
            result = caesar_cipher(temp, caesar_key)
            
        print(f"\nMessage chiffré: {result}")
        
    elif choice == "2":
        message = input("Entrez le message à déchiffrer: ")
        caesar_key = int(get_valid_input("Clé César (0-25): ", validate_caesar_key))
        affine_a = int(get_valid_input("Clé Affine a (premier avec 26): ", validate_affine_a))
        affine_b = int(get_valid_input("Clé Affine b (0-25): ", validate_affine_b))
        
        print("\nOrdre de déchiffrement:")
        print("1. Affine puis César")
        print("2. César puis Affine")
        order = input("Votre choix (1-2): ")
        
        if order == "1":
            # Affine puis César
            temp = affine_decipher(message, affine_a, affine_b)
            result = caesar_decipher(temp, caesar_key)
        else:
            # César puis Affine
            temp = caesar_decipher(message, caesar_key)
            result = affine_decipher(temp, affine_a, affine_b)
            
        print(f"\nMessage déchiffré: {result}")
        
    elif choice == "3":
        sys.exit(0)
    else:
        print("Choix invalide")

if __name__ == "__main__":
    while True:
        main()
        input("\nAppuyez sur Entrée pour continuer...") 