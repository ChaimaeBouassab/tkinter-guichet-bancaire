import tkinter as tk
from tkinter import messagebox

# Définition de la fenêtre principale
window = tk.Tk()
window.title("GAB Guichet automatique bancaire")
window.geometry("300x400")

tentativePin = 0  
maxTentativePin = 3  
withdrawal_window = None

# Fonction pour vérifier l'authentification
def authenticate():
    global tentativePin
    global balance
    card_number = card_number_entry.get()
    pin = pin_entry.get()

    # Vérification des identifiants
    if card_number == "1111" and pin == "1234":  
        tentativePin=0
        show_withdrawal_window()   # afficher la fenêtre de retrait lorsque l'authentification réussit.
    else:
        tentativePin=tentativePin+1
        if tentativePin==maxTentativePin:
            messagebox.showerror("Erreur", "compte blocke")
            



# Fonction pour afficher la fenêtre de retrait
def show_withdrawal_window():
    window.withdraw()
    withdrawal_window = tk.Toplevel(window)
    withdrawal_window.title("Retrait")
    withdrawal_window.geometry("300x200")

balance = 10000  
max_withdrawal_amount = 5000

def withdraw_amount():
    amount = amount_entry.get()
    if amount.isdigit():
        amount = int(amount)
        if amount <= balance:
            if amount <= max_withdrawal_amount:
                balance -= amount
                messagebox.showinfo("Succès", "Retrait effectué avec succès. Nouveau solde : " + str(balance))
            else:
                messagebox.showerror("Erreur", "Le montant demandé dépasse la limite de retrait quotidienne.")
        else:
            messagebox.showerror("Erreur", "Solde insuffisant.")
    else:
        messagebox.showerror("Erreur", "Montant non valide.")

    withdrawal_window.destroy()  

# Éléments graphiques pour l'authentification
card_number_label = tk.Label(window, text="Numéro de carte bancaire:")
card_number_entry = tk.Entry(window)
pin_label = tk.Label(window, text="Code PIN:")
pin_entry = tk.Entry(window, show="*")
login_button = tk.Button(window, text="Se connecter", command=authenticate)

  # Éléments graphiques pour le retrait
amount_label = tk.Label(withdrawal_window, text="Montant de retrait:")
amount_entry = tk.Entry(withdrawal_window)
withdraw_button = tk.Button(withdrawal_window, text="Retrait", command=withdraw_amount)

# Placement des éléments graphiques
card_number_label.pack()
card_number_entry.pack()
pin_label.pack()
pin_entry.pack()
login_button.pack()
amount_label.pack()
amount_entry.pack()
withdraw_button.pack()

# Lancement de la boucle principale
window.mainloop()
