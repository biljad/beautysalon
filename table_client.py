import sqlite3

connection = sqlite3.connect("beauty_salon.db")
cursor = connection.cursor()

# Insert new client
def insert_client(jmbg, first_name, last_name, date_of_birth):
    sql_comm = "INSERT INTO client (jmbg, first_name, last_name, date_of_birth) VALUES (?,?,?,?);"
    connection.execute(sql_comm, (jmbg, first_name, last_name, date_of_birth))
    connection.commit()
    print("Unijeli smo dodali novog klijenta.")

# Change client info
def change_client(id, jmbg, first_name, last_name, date_of_birth):
    sql_comm = "UPDATE client SET jmbg=?, first_name=?, last_name=?, date_of_birth=? WHERE id=?;"
    connection.execute(sql_comm, (id, jmbg, first_name, last_name, date_of_birth))
    connection.commit()
    print("Podaci o klijentu su izmjenjeni.")
    res = connection.cursor()
    sql_comm = "UPDATE client SET id=?, jmbg=?, first_name=?, last_name=?, date_of_birth=?;"
    client = (id, jmbg, first_name, last_name, date_of_birth)
    res.execute(sql_comm, client)
    connection.commit()
    print("Uspiješno ste izmjenili informacije o klijentu.")

# Delete client
def delete_client(id):
    sql_comm = "DELETE FROM client WHERE id=?;"
    connection.execute(sql_comm, (id))
    connection.commit()
    print("Podaci o client su uspiješno obrisani.")

# Select client
def select_client():
    sql_select="""SELECT * FROM client;"""
    cursor.execute(sql_select)
    result=cursor.fetchall()
    for x in result:
        print(x)

# Show menu
def show_menu(connection):
    print("Prikazi opcije")
    print("1. Unos podataka o klijentu")
    print("2. Izmjena podataka o klijentu")
    print("3. Brisanje klijenta")
    print("4. Prikazivanje svih unesenih podataka")
    menu = input("Izaberi opciju:")
    if menu == "1":
        number_of_client = int(input("Unesite broj klijenata koliko zelite da unesete? "))
        if number_of_client < 1:
            print("Unesite veci broj od 0.")
            number_of_client = int(input("Unesite broj klijeenata koliko zelite? "))
        for i in range(number_of_client):
            print("Dodajte novog klijenta. ")
            jmbg = input("Unesite jmbg: ")
            first_name = input("Unesi ime: ")
            last_name = input("Unesi prezime: ")
            date_of_birth = input("Unesi datum rodjenja(format:dd/mm/yyyy): ")
            insert_client(jmbg, first_name, last_name, date_of_birth)
    elif menu == "2":
        id = int(input("Unesite id klijenta kojeg zelite da izmjenite: "))
        jmbg = int(input("Unesite jmbg klijenta: "))
        first_name = input("Unesite ime: ")
        last_name = input("Unesite prezime: ")
        date_of_birth = input("Unesite datum rodjenja: ")
        change_client(id, jmbg, first_name, last_name, date_of_birth)
    elif menu == "3":
        print("Brisanje informacija o klijentu.")
        id = input("Unesite id klijenta kojeg zelite da obrisete: ")
        delete_client(id)
    elif menu == "4":
        print("Prikaz tabele klijenata: ")
        select_client()
    else:
        print("Molimo Vas da unesete broj od 1 do 4, kako bi program mogao da nastavi sa radom.")

while True:
    show_menu(connection)

