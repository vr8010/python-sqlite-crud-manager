import sqlite3

con = sqlite3.connect("company.db")
cur = con.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS manager(
    id INTEGER PRIMARY KEY,
    name TEXT,
    salary INTEGER
)
""")

while True:
    print("\n===== Manager CRUD =====")
    print("1. Add Data")
    print("2. Show Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("5. Exit")

    choice = input("Enter choice: ")

    # ADD DATA
    if choice == "1":
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        salary = int(input("Enter Salary: "))

        cur.execute(
            "INSERT INTO manager (id, name, salary) VALUES (?, ?, ?)",
            (id, name, salary)
        )
        con.commit()
        print("Data Added!")

    # SHOW DATA
    elif choice == "2":
        cur.execute("SELECT * FROM manager")
        data = cur.fetchall()

        print("\nID  Name  Salary")
        for row in data:
            print(row[0], row[1], row[2])

    # UPDATE DATA
    elif choice == "3":
        id = int(input("Enter ID to update: "))
        name = input("Enter new name: ")
        salary = int(input("Enter new salary: "))

        cur.execute(
            "UPDATE manager SET name=?, salary=? WHERE id=?",
            (name, salary, id)
        )
        con.commit()
        print("Data Updated!")

    # DELETE DATA
    elif choice == "4":
        id = int(input("Enter ID to delete: "))

        cur.execute("DELETE FROM manager WHERE id=?", (id,))
        con.commit()
        print("Data Deleted!")

    # EXIT
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")

con.close()