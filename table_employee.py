import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

# Insert new employee
def insert_employee(jmbg, first_name, last_name, date_of_birth, date_of_employment, work_position):
    sql_comm = "INSERT INTO employee (jmbg, first_name, last_name, date_of_birth, date_of_employment, work_position) VALUES (?,?,?,?,?,?);"
    connection.execute(sql_comm, (jmbg, first_name, last_name, date_of_birth, date_of_employment, work_position))
    connection.commit()
    print("Unijeli smo novog zaposlenika.")

# Change employee info
def change_employee(id, jmbg, first_name, last_name, date_of_birth, date_of_employment, work_position):
    sql_comm = "UPDATE employee SET jmbg=?, first_name=?, last_name=?, date_of_birth=?, date_of_employment=?, work_position=? WHERE id=?;"
    connection.execute(sql_comm, (id, jmbg, first_name, last_name, date_of_birth, date_of_employment, work_position))
    connection.commit()
    print("Podaci o zaposleniku su izmjenjeni.")
    res = connection.cursor()
    sql_comm = "UPDATE employee SET id=?, jmbg=?, first_name=?, last_name=?, date_of_birth=?, date_of_employment=?, work_position=?;"
    employee = (id, jmbg, first_name, last_name, date_of_birth, date_of_employment, work_position)
    res.execute(sql_comm, employee)
    connection.commit()
    print("Uspiješno ste izmjenili informacije o zaposleniku.")

# Delete employee
def delete_employee(id):
    sql_comm = "DELETE FROM employee WHERE id=?;"
    connection.execute(sql_comm, (id))
    connection.commit()
    print("Podaci o zaposelniku su uspiješno obrisani.")

# Select employee
def select_employee():
    sql_select="""SELECT * FROM employee;"""
    cursor.execute(sql_select)
    result=cursor.fetchall()
    for x in result:
        print(x)

# Show menu
def show_menu(connect):
    print("Prikazi opcije")
    print("1. Unos podataka o zapoleniku")
    print("2. Izmjena podataka o zaposleniku")
    print("3. Brisanje zaposlenog")
    print("4. Prikazivanje svih unesenih podataka")
    menu = input("Izaberi opciju:")
    if menu == "1":
        number_of_employee = int(input("Unesite broj zaposlenih koliko zelite? "))
        if number_of_employee < 1:
            print("Unesite veci broj od 0.")
            number_of_employee = int(input("Unesite broj zaposlenih koliko zelite? "))
        for i in range(number_of_employee):
            print("Dodajte novog zaposlenika. ")
            jmbg = input("Unesite jmbg: ")
            first_name = input("Unesi ime: ")
            last_name = input("Unesi prezime: ")
            date_of_birth = input("Unesi datum rodjenja(format:dd/mm/yyyy): ")
            date_of_employment = input("Unesi datum zaposlenja(format:dd/mm/yyyy): ")
            work_position = input("Unesi radnu poziciju: ")
            insert_employee(jmbg, first_name, last_name, date_of_birth, date_of_employment, work_position)
    elif menu == "2":
        id = int(input("Unesite id radnika kojeg zelite da izmjenite: "))
        jmbg = int(input("Unesite jmbg radnika: "))
        first_name = input("Unesite ime: ")
        last_name = input("Unesite prezime: ")
        date_of_birth = input("Unesite datum rodjenja: ")
        date_of_employment = input("Unesite datum zapošljavanja: ")
        work_position = input("Unesite radnu poziciju: ")
        change_employee(id, jmbg, first_name, last_name, date_of_birth, date_of_employment, work_position)
    elif menu == "3":
        print("Brisanje informacija o zaposleniku.")
        id = input("Unesite id zaposlenika kojeg zelite da obrisete: ")
        delete_employee(id)
    elif menu == "4":
        print("Prikaz tabele zaposlenih")
        select_employee()
    else:
        print("Molimo Vas da unesete broj od 1 do 4, kako bi program mogao da nastavi sa radom.")

while True:
    show_menu(connection)
    connection.close()
    break
