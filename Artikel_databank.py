from pymongo import MongoClient
import tkinter as tk
from tkinter import messagebox

def artikel_hinzufügen(collection, artikel_nr, name, hersteller, preis):
    artikel_daten = {
        'artikel_nr': artikel_nr.get(),
        'name': name.get(),
        'hersteller': hersteller.get(),
        'preis': preis.get()
    }

    collection.insert_one(artikel_daten)
    messagebox.showinfo("Erfolg", "Artikel hinzugefügt")

    # Eingabefelder leeren
    artikel_nr.set("")
    name.set("")
    hersteller.set("")
    preis.set("")

def artikel_suchen(collection, artikel_nr):
    artikel = collection.find_one({'artikel_nr': artikel_nr.get()})

    if artikel:
        messagebox.showinfo("Artikel gefunden", str(artikel))
    else:
        messagebox.showinfo("Fehler", "Artikel nicht mit dieser Nummer gefunden")

def main():
    database = MongoClient('mongodb://localhost:27017/')['artikellverwaltung_db']
    collection = database['artikel']

    root = tk.Tk()
    root.geometry("800x600")

    artikel_nr = tk.StringVar()
    name = tk.StringVar()
    hersteller = tk.StringVar()
    preis = tk.StringVar()

    tk.Label(root, text="Artikelnummer").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    tk.Entry(root, textvariable=artikel_nr).grid(row=0, column=1, padx=10, pady=10, sticky="w")

    tk.Label(root, text="Name").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    tk.Entry(root, textvariable=name).grid(row=1, column=1, padx=10, pady=10, sticky="w")

    tk.Label(root, text="Hersteller").grid(row=2, column=0, padx=10, pady=10, sticky="e")
    tk.Entry(root, textvariable=hersteller).grid(row=2, column=1, padx=10, pady=10, sticky="w")

    tk.Label(root, text="Preis").grid(row=3, column=0, padx=10, pady=10, sticky="e")
    tk.Entry(root, textvariable=preis).grid(row=3, column=1, padx=10, pady=10, sticky="w")

    tk.Button(root, text="Artikel hinzufügen", command=lambda: artikel_hinzufügen(collection, artikel_nr, name, hersteller, preis)).grid(row=4, column=0, columnspan=2, pady=10)
    tk.Button(root, text="Artikel suchen", command=lambda: artikel_suchen(collection, artikel_nr)).grid(row=5, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()