import sqlite3

connection = sqlite3.connect("beauty_salon.db")
cursor = connection.cursor()

# Insert new price list
def insert_price_list(nail_extension, nail_correction, permanent_varnish, make_up, waxing):
    sql_comm = "INSERT INTO price_list (nail_extension, nail_correction, permanent_varnish, make_up, waxing) VALUES (?,?,?,?,?);"
    connection.execute(sql_comm, (nail_extension, nail_correction, permanent_varnish, make_up, waxing))
    connection.commit()
    print("Unijeli smo dodali novu cijenu usluge.")

# Change price list info
def change_price_list(id, nail_extension, nail_correction, permanent_varnish, make_up, waxing):
    sql_comm = "UPDATE price_list SET nail_extension=?, nail_correction=?, permanent_varnish=?, make_up=?, waxing=? WHERE id=?;"
    connection.execute(sql_comm, (id, nail_extension, nail_correction, permanent_varnish, make_up, waxing))
    connection.commit()
    print("Podaci o cjenovniku su izmjenjeni.")
    res = connection.cursor()
    sql_comm = "UPDATE price_list SET id=?, nail_extension=?, nail_correction=?, permanent_varnish=?, make_up=?, waxing=?;"
    price_list = (id, nail_extension, nail_correction, permanent_varnish, make_up, waxing)
    res.execute(sql_comm, price_list)
    connection.commit()
    print("Uspiješno ste izmjenili cjenovnik usluge.")

# Delete price list
def delete_services(id):
    sql_comm = "DELETE FROM price_list WHERE id=?;"
    connection.execute(sql_comm, (id))
    connection.commit()
    print("Podaci o cjenovniku su uspiješno obrisani.")

# Select price list
def select_services():
    sql_select="""SELECT * FROM price_list;"""
    cursor.execute(sql_select)
    result=cursor.fetchall()
    for x in result:
        print(x)

# Show menu
def show_menu(connection):
    print("Prikazi opcije")
    print("1. Unos podataka o cjenovniku")
    print("2. Izmjena podataka o cjenovniku")
    print("3. Brisanje cjenovnika")
    print("4. Prikazivanje svih unesenih podataka")
    menu = input("Izaberi opciju:")
    if menu == "1":
            print("Dodajte novu cijenu. ")
            nail_extension = input("Unesite cijenu usluge nadogradnje noktiju: ")
            nail_correction = input("Unesite cijenu usluge popravke noktiju: ")
            permanent_varnish = input("Unesite cijenu usluge trajnog laka: ")
            make_up = input("Unesite cijenu usluge sminkanja: ")
            waxing = input("Unesite cijenu usluge depilacije: ")
            insert_price_list(nail_extension, nail_correction, permanent_varnish, make_up, waxing)
    elif menu == "2":
        id = int(input("Unesite id cijene kojeg zelite da izmjenite: "))
        nail_extension = input("Unesite novu cijenu usluge nadogradnje noktiju: ")
        nail_correction = input("Unesite novu cijenu usluge popravke noktiju: ")
        permanent_varnish = input("Unesite novu cijenu usluge trajnog laka: ")
        make_up = input("Unesite novu cijenu usluge sminkanja: ")
        waxing = input("Unesite novu cijenu usluge depilacije: ")
        change_price_list(id, nail_extension, nail_correction, permanent_varnish, make_up, waxing)
    elif menu == "3":
        print("Brisanje informacija o cjenovniku.")
        id = input("Unesite id cijene kojeg zelite da obrisete: ")
        delete_services(id)
    elif menu == "4":
        print("Prikaz tabele cijene: ")
        select_services()
    else:
        print("Molimo Vas da unesete broj od 1 do 4, kako bi program mogao da nastavi sa radom.")

while True:
    show_menu(connection)
    connection.close()
    break

