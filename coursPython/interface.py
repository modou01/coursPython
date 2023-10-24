import tkinter as tk

# Fonction appelée lorsque le bouton "Valider" est pressé
def valider_inscription():
    # Récupérer les données des champs de saisie
    pseudo = entry_pseudo.get() #recuperer les donnée entrées
    mdp = entry_mdp.get()
    email = entry_email.get()
    
    # Afficher les données dans le terminal
    print("Inscription validée :")
    print(f"Pseudo : {pseudo}")
    print(f"Mot de passe : {mdp}")
    print(f"Email : {email}")

# Création de la fenêtre principale
fenetre = tk.Tk() #une instance de la fenêtre principale de votre application.
fenetre.title("Inscription")

# Création des libellés et des champs de saisie pour Pseudo
# une manière de rentrée les données de saisir quoi
label_pseudo = tk.Label(fenetre, text="Pseudo :") # crée un libellé avec le texte "Pseudo 
label_pseudo.pack()

entry_pseudo = tk.Entry(fenetre) #crée un champ de saisie pour le pseudo.
entry_pseudo.pack()

# Création des libellés et des champs de saisie pour Mot de passe
label_mdp = tk.Label(fenetre, text="Mot de passe :")
label_mdp.pack()

entry_mdp = tk.Entry(fenetre, show="*")  # Montre des étoiles pour masquer le mot de passe
entry_mdp.pack()

# Création des libellés et des champs de saisie pour Email
label_email = tk.Label(fenetre, text="Email :")
label_email.pack()

entry_email = tk.Entry(fenetre)
entry_email.pack()

# Bouton de validation
bouton_valider = tk.Button(fenetre, text="Valider", command=valider_inscription)
bouton_valider.pack()

# Démarrage de la boucle principale de la fenêtre
fenetre.mainloop()
