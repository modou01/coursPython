# Définition de la fonction pour saisir les informations
def saisir_informations():
    nom_famille = input("Entrez votre nom de famille : ")
    prenom = input("Entrez votre prénom : ")
    age = input("Entrez votre âge : ")
    taille = input("Entrez votre taille : ")
    fruits_preferes = input("Entrez une liste de vos fruits pref : ")
    message = input(" un message de salutation : ")
    produit = input("Entrez les propriétés d'un produit : ")

    # Affichage des informations
    print("\nInformations personnelles :")
    print(f"Nom de famille : {nom_famille}")
    print(f"Prénom : {prenom}")
    print(f"Âge : {age} ans")
    print(f"Taille : {taille} cm")
    print(f"Fruits préférés : {fruits_preferes}")
    print(f"Message de salutation : {message}")
    print(f"Propriétés du produit : {produit}")

# Appel de la fonction pour saisir et afficher les informations
saisir_informations()
