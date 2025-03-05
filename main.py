import json


OFFERS_FILE = "offers.json"
PRODUCTS_FILE = "products.json"
CUSTOMERS_FILE = "customers.json"


def load_data(filename):
    """Load data from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Error decoding {filename}. Check file format.")
        return []


def save_data(filename, data):
    """Save data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# TODO: Implementirajte funkciju za kreiranje nove ponude.
def create_new_offer(offers, products, customers):
    """
    Prompt user to create a new offer by selecting a customer, entering date,
    choosing products, and calculating totals.
    """
    # Omogućite unos kupca --> Kupac upise broj ispred a vi onda pokupite te podatke
    #       za ovo bi dobro dosla jedna while True petlja s brake izlazom.
    # Izračunajte sub_total, tax i total
    # Dodajte novu ponudu u listu offers



    
    pass


# TODO: Implementirajte funkciju za upravljanje proizvodima.
def manage_products(products):
    """
    Allows the user to add a new product or modify an existing product.
    """
    # Omogućite korisniku izbor između dodavanja ili izmjene proizvoda
    # Za dodavanje: unesite podatke o proizvodu i dodajte ga u listu products
    # Za izmjenu: selektirajte proizvod i ažurirajte podatke
    pass


# TODO: Implementirajte funkciju za upravljanje kupcima.
def manage_customers(customers):
    """
    Allows the user to add a new customer or view all customers.
    """
    # Za dodavanje: omogući unos imena kupca, emaila i unos VAT ID-a
costumer_list = []
manage_customers(costumer_list)

while True:  
    
    print('-------------')
    print('IZBORNIK')
    print('-------------')
 
    print("1. Dodaj novog kupca")
    print("2. Prikaži sve kupce")
    print("3. Izlaz")
    choice = input('Odaberite opciju: ')
    
    
    if choice == "1":
        name = input('Unesite ime kupca: ')
        email = input('Unesite email: ')
        vat_id = input('Unesite ID kupca: ')
        

        costumer = {
                "Ime": name,
                "Email": email,
                "ID": vat_id

        }
        costumer_list.append(costumer)
        print('Kupac uspjesno dodan!\n')

    
    
    elif choice == "2":
        if not costumer:
            print('Nema unesenih kupaca.')
        else:
            print("Lista svih kupaca:")
            for idx, costumer in enumerate(costumer, start=1):
                print(f'{idx}. {costumer['Ime']}, {costumer["Email"]}, {costumer["ID"]}')
    elif choice == "3":
        print('Izlaz iz programa')
        break
    else:
        print('Krivi odabir, pokusajte ponovno')



    # Za pregled: prikaži listu svih kupaca
    pass


# TODO: Implementirajte funkciju za prikaz ponuda.
def display_offers(offers):
    """
    Display all offers, offers for a selected month, or a single offer by ID.
    """
from datetime import datetime

OFFERS_FILE = "offers.json"

def load_offers_from_file():
    """ Učitava ponude iz JSON datoteke ako postoji. """
    try:
        with open(OFFERS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def display_offers(offers):
    """
    Omogućuje pregled svih ponuda, filtriranje po mjesecu ili prikaz pojedinačne ponude po ID-u.
    """
    if not offers:
        print("Nema dostupnih ponuda.")
        return

    while True:
        print("\n Odaberite način pregleda ponuda:")
        print("1. Prikaz svih ponuda")
        print("2. Prikaz ponuda za određeni mjesec")
        print("3. Prikaz pojedinačne ponude (prema ID-u)")
        print("4. Povratak")

        choice = input("Unesite broj opcije: ")

        if choice == "1":
            print("\n Sve ponude:")
            for idx, offer in enumerate(offers, start=1):
                print(f"{idx}. {offer['datum']} - {offer['kupac']} - {offer['total']} kn")

        elif choice == "2":
            month = input("Unesite mjesec (MM format, npr. 02 za Veljaču): ")
            filtered_offers = [o for o in offers if datetime.strptime(o['datum'], "%Y-%m-%d").strftime("%m") == month]
            
            if not filtered_offers:
                print(" Nema ponuda za odabrani mjesec.")
            else:
                print(f"\n Ponude za mjesec {month}:")
                for idx, offer in enumerate(filtered_offers, start=1):
                    print(f"{idx}. {offer['datum']} - {offer['kupac']} - {offer['total']} kn")

        elif choice == "3":
            try:
                offer_id = int(input("Unesite ID ponude (redni broj s popisa): ")) - 1
                if 0 <= offer_id < len(offers):
                    offer = offers[offer_id]
                    print("\n Detalji ponude:")
                    print(f" ID: {offer_id + 1}")
                    print(f" Kupac: {offer['kupac']} ({offer['email']})")
                    print(f" Datum: {offer['datum']}")
                    print(f" Artikli:")
                    for item in offer["proizvodi"]:
                        print(f"{item['naziv']} ({item['kolicina']} kom) - {item['cijena']} kn/kom")
                    print(f" Subtotal: {offer['sub_total']} kn")
                    print(f" Porez: {offer['tax']} kn")
                    print(f" Ukupno: {offer['total']} kn")
                else:
                    print(" Nevažeći ID. Pokušajte ponovno.")
            except ValueError:
                print(" Molimo unesite broj.")

        elif choice == "4":
            break

        else:
            print(" Nevažeća opcija. Pokušajte ponovno.")   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # Omogućite izbor pregleda: sve ponude, po mjesecu ili pojedinačna ponuda
    # Prikaz relevantnih ponuda na temelju izbora
    pass


# Pomoćna funkcija za prikaz jedne ponude
def print_offer(offer):
    """Display details of a single offer."""
    print(f"Ponuda br: {offer['offer_number']}, Kupac: {offer['customer']['name']}, Datum ponude: {offer['date']}")
    print("Stavke:")
    for item in offer["items"]:
        print(f"  - {item['product_name']} (ID: {item['product_id']}): {item['description']}")
        print(f"    Kolicina: {item['quantity']}, Cijena: ${item['price']}, Ukupno: ${item['item_total']}")
    print(f"Ukupno: ${offer['sub_total']}, Porez: ${offer['tax']}, Ukupno za platiti: ${offer['total']}")


def main():
    # Učitavanje podataka iz JSON datoteka
    offers = load_data(OFFERS_FILE)
    products = load_data(PRODUCTS_FILE)
    customers = load_data(CUSTOMERS_FILE)

    while True:
        print("\nOffers Calculator izbornik:")
        print("1. Kreiraj novu ponudu")
        print("2. Upravljanje proizvodima")
        print("3. Upravljanje korisnicima")
        print("4. Prikaz ponuda")
        print("5. Izlaz")
        choice = input("Odabrana opcija: ")

        if choice == "1":
            create_new_offer(offers, products, customers)
        elif choice == "2":
            manage_products(products)
        elif choice == "3":
            manage_customers(customers)
        elif choice == "4":
            display_offers(offers)
        elif choice == "5":
            # Pohrana podataka prilikom izlaza
            save_data(OFFERS_FILE, offers)
            save_data(PRODUCTS_FILE, products)
            save_data(CUSTOMERS_FILE, customers)
            break
        else:
            print("Krivi izbor. Pokusajte ponovno.")


if __name__ == "__main__":
    main()
