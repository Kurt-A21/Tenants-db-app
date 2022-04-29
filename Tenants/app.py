import sqlite3

conn = sqlite3.connect("Tenants Paymenst.db")

c = conn.cursor()

print(" \n\n                           Seaview Apartments")
print("_____________________________________________________________________________\n")
print("* Monthly Rent is R4000,00 *")
print("To view all tenants that did not pay last month\nType 'J'\n\n" +
      "To view all tenants with outstanding payments for this month\nType 'F'\n\n" +
      "To display all tenants that will receive a discount for next month\nType 'D'\n")

option = input("Enter value: ")

if option == "J":
    print("January Outstanding Rent: \n")
    c.execute(
        'SELECT id, Tenant_Name FROM Seaview_Apartment WHERE Jan_Rent is NULL')
    myresult = c.fetchall()
    for row in myresult:
        print(row)
    c.execute(
        'select Jan_Rent, count(*) from Seaview_Apartment where Jan_Rent is NULL'
    )
    myresult = c.fetchall()
    for row in myresult:
        print("\nThe number of tenants with outstading rent: ")
        print(row)

elif option == "F":
    print("February Outstanding Rent: \n")
    c.execute(
        "SELECT id, Tenant_Name FROM Seaview_Apartment WHERE Feb_Rent is NULL")
    myresult = c.fetchall()
    for row in myresult:
        print(row)
        c.execute(
            'select Feb_Rent, count(*) from Seaview_Apartment where Feb_Rent is NULL')
    myresult = c.fetchall()
    for row in myresult:
        print("\nThe number of tenants with outstading rent: ")
        print(row)

elif option == "D":
    print("Tenants who will receive a R200.00 discount on rent next month are: \n")
    c.execute(
        "SELECT id, Tenant_Name FROM Seaview_Apartment WHERE Jan_Rent AND Feb_Rent is not NULL")
    myresult = c.fetchall()
    for row in myresult:
        print(row)
