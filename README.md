# Projet de Sécurité - Démonstration de Chiffrement

Ce projet implémente un système complet de démonstration et d'apprentissage des algorithmes de chiffrement classiques et modernes.

## 🚀 Fonctionnalités

### Interface Web Interactive (`index.html`)
- **Interface moderne** avec design responsive
- **Algorithmes supportés** :
  - Chiffrement de César
  - Chiffrement Affine
  - AES (simulation)
  - RSA (simulation)
  - Signatures numériques
  - Double chiffrement (César + Affine)
- **Visualisations interactives** :
  - Alphabet animé
  - Roue d'alphabet interactive
  - Flux de transformation des caractères
  - Analyse de fréquence avec graphiques
- **Explications étape par étape** pour chaque algorithme
- **Contrôles de visualisation** pour personnaliser l'expérience

### Interface Python (`main.py`)
- **Double chiffrement** César-Affine
- **Validation des clés** de chiffrement
- **Analyse de fréquence** des lettres
- **Attaque par force brute** sur le chiffrement César

## 🛠️ Installation et Utilisation

### Interface Web (Recommandée)
1. Ouvrez simplement le fichier `index.html` dans votre navigateur
2. Aucune installation requise
3. Interface complète avec visualisations interactives

### Interface Python
1. Assurez-vous d'avoir Python 3.x installé
2. Exécutez : `python main.py`
3. Suivez les instructions à l'écran

## 📚 Explication des Algorithmes

### Chiffrement de César
- Déplace chaque lettre d'un nombre fixe de positions dans l'alphabet
- Clé : nombre de positions (0-25)

### Chiffrement Affine
- Utilise une transformation mathématique : y = (a * x + b) mod 26
- Clés : a (premier avec 26) et b (0-25)

### Double Chiffrement
Combine César et Affine pour renforcer la sécurité :
1. César puis Affine
2. Affine puis César

## 🎨 Visualisations

Le projet inclut plusieurs types de visualisations éducatives :
- **Alphabet Animé** : Montre la transformation des caractères
- **Roue d'Alphabet** : Représentation circulaire interactive
- **Flux de Caractères** : Diagramme de transformation étape par étape
- **Analyse de Fréquence** : Graphiques en barres des fréquences

## 🔒 Sécurité

- Le double chiffrement rend l'analyse de fréquence plus difficile
- L'ordre des algorithmes ajoute une couche de complexité
- L'attaque par force brute est inefficace contre le double chiffrement

## 📁 Structure du Projet

```
projet-sécurité/
├── index.html          # Interface web principale
├── main.py            # Interface Python
├── cipher_functions.py # Fonctions de chiffrement
├── README.md          # Documentation
└── tp.html           # Version alternative
```

## 🎯 Exemple d'utilisation

### Interface Web
1. Ouvrez `index.html` dans votre navigateur
2. Choisissez un algorithme de chiffrement
3. Entrez votre message
4. Observez les visualisations en temps réel
5. Explorez les explications étape par étape

### Interface Python
1. Chiffrement :
   - Message : "HELLO"
   - Clé César : 3
   - Clé Affine : a=5, b=7
   - Ordre : César puis Affine
   - Résultat : "QJXXT"

2. Déchiffrement :
   - Message chiffré : "QJXXT"
   - Mêmes clés
   - Ordre inverse : Affine puis César
   - Résultat : "HELLO"

## 🤝 Contribution

Ce projet est ouvert aux contributions ! N'hésitez pas à :
- Ajouter de nouveaux algorithmes
- Améliorer les visualisations
- Corriger des bugs
- Améliorer la documentation

## 📄 Licence

Ce projet est destiné à des fins éducatives. 