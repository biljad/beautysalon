import sqlite3

connection = sqlite3.connect("beauty_salon.db")
cursor = connection.cursor()

# Insert new services
def insert_services(nail_extension, nail_correction, permanent_varnish, make_up, waxing):
    sql_comm = "INSERT INTO services (nail_extension, nail_correction, permanent_varnish, make_up, waxing) VALUES (?,?,?,?,?);"
    connection.execute(sql_comm, (nail_extension, nail_correction, permanent_varnish, make_up, waxing))
    connection.commit()
    print("Unijeli smo dodali novu uslugu.")

# Change services info
def change_services(id, nail_extension, nail_correction, permanent_varnish, make_up, waxing):
    sql_comm = "UPDATE services SET nail_extension=?, nail_correction=?, permanent_varnish=?, make_up=?, waxing=? WHERE id=?;"
    connection.execute(sql_comm, (id, nail_extension, nail_correction, permanent_varnish, make_up, waxing))
    connection.commit()
    print("Podaci o uslugi su izmjenjeni.")
    res = connection.cursor()
    sql_comm = "UPDATE services SET id=?, nail_extension=?, nail_correction=?, permanent_varnish=?, make_up=?, waxing=?;"
    services = (id, nail_extension, nail_correction, permanent_varnish, make_up, waxing)
    res.execute(sql_comm, services)
    connection.commit()
    print("Uspiješno ste izmjenili informacije o uslugi.")

# Delete services
def delete_services(id):
    sql_comm = "DELETE FROM services WHERE id=?;"
    connection.execute(sql_comm, (id))
    connection.commit()
    print("Podaci o uslugi su uspiješno obrisani.")

# Select services
def select_services():
    sql_select="""SELECT * FROM services;"""
    cursor.execute(sql_select)
    result=cursor.fetchall()
    for x in result:
        print(x)

# Show menu
def show_menu(connection):
    print("Prikazi opcije")
    print("1. Unos podataka o uslugi")
    print("2. Izmjena podataka o uslugi")
    print("3. Brisanje usluge")
    print("4. Prikazivanje svih unesenih podataka")
    menu = input("Izaberi opciju:")
    if menu == "1":
            print("Dodajte novu uslugu. ")
            nail_extension = input("Unesite kolicinu usluge nadogradnje noktiju: ")
            nail_correction = input("Unesite kolicinu usluge popravke noktiju: ")
            permanent_varnish = input("Unesite kolicinu usluge trajnog laka: ")
            make_up = input("Unesite kolicinu usluge sminkanja: ")
            waxing = input("Unesite kolicinu usluge depilacije: ")
            insert_services(nail_extension, nail_correction, permanent_varnish, make_up, waxing)
    elif menu == "2":
        id = int(input("Unesite id usluge kojeg zelite da izmjenite: "))
        nail_extension = input("Unesite novu kolicinu usluge nadogradnje noktiju: ")
        nail_correction = input("Unesite novu kolicinu usluge popravke noktiju: ")
        permanent_varnish = input("Unesite novu kolicinu usluge trajnog laka: ")
        make_up = input("Unesite novu kolicinu usluge sminkanja: ")
        waxing = input("Unesite novu kolicinu usluge depilacije: ")
        change_services(id, nail_extension, nail_correction, permanent_varnish, make_up, waxing)
    elif menu == "3":
        print("Brisanje informacija o uslugama.")
        id = input("Unesite id usluge kojeg zelite da obrisete: ")
        delete_services(id)
    elif menu == "4":
        print("Prikaz tabele usluga: ")
        select_services()
    else:
        print("Molimo Vas da unesete broj od 1 do 4, kako bi program mogao da nastavi sa radom.")

while True:
    show_menu(connection)
    connection.close()
    break

