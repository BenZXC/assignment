import os


ITEMS = (("MacBook Pro", "Apple", 2),
         ("AC1200 Wireless Adapter", "ALFA Network", 4),
         ("Jetson Nano Developer Kit", "NVIDIA", 3),
         ("WRT1900AC Dual-Band Wi-Fi Router", "Linksys", 2),
         ("RoboMaster EP", "DJI", 2))


# Index represented in tuple ITEMS
INDEX_ITEM_NAME = 0
INDEX_ITEM_BRAND = 1
INDEX_ITEM_TOTAL_QUANTITY = 2

# Index represented in user item tuple inside key part in user_borrow_record dictionary
INDEX_USER_BORROW_RECORD = 0
INDEX_ITEM_BORROW_RECORD = 1

# Function ID mapped with name
FUNCTION_BORROW_ITEM = 0
FUNCTION_RETURN_ITEM = 1
DISPLAY_USER_RECORDS = 2
DISPLAY_ALL_RECORDS = 3

debug = False

# txt
working_directory = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
user_list_file = open(working_directory + "/borrowers.txt", "r")
# you may implement other necessary functions here


def dmsg(msg):
    if debug:
        print(f"\033[96m[debug]\033[0m {msg}")


def menu():
    print("No. | Function")
    print("0   | Borrow Item")
    print("1   | Return Item")
    print("2   | Display User Records")
    print("3   | Display All Records")
    while True:
        menu_input = int(input("Please input your choice. (0 - 3, Enter to exit):"))
        if menu_input in range(4):
            return menu_input
        else:
            print("Invalid Function input")


def borrow_items(item_no, borrowed_quantity, name):

    for user, quantity in user_borrow_record.items():
        if (user[0] == name) and (int(user[1]) == int(item_no)):
            dmsg("update record")
            dmsg(f"item_no = {item_no}")
            dmsg(f"new_quantity = {borrowed_quantity}")
            dmsg(f"name = {name}")
            dmsg(f"user = {name}")
            dmsg(f"quantity = {name}")
            user_borrow_record[(name, item_no)] = quantity + borrowed_quantity
            dmsg(user_borrow_record)
            return True
    dmsg("create record")
    dmsg(f"item_no = {item_no}")
    dmsg(f"new_quantity = {borrowed_quantity}")
    dmsg(f"name = {name}")
    user_borrow_record.update({(name, item_no): borrowed_quantity})
    dmsg(f"input_data = {[name, item_no, borrowed_quantity]}")
    dmsg(f"user_borrow_record = {user_borrow_record}")


def returning_item(borrower_name):

    result = dict()
    for key, value in user_borrow_record.items():
        if key[INDEX_USER_BORROW_RECORD] == borrower_name:
            result[key] = value

    for k, i in result.items():
        print(f"Item(s) {borrower_name} had borrowed: ")
        print("Item No. | Item Name                               |Qty.Borrowed")
        print(f"{k[1]:>7}. | {ITEMS[k[1]][INDEX_ITEM_NAME]:<41} |  {i:>8}")
        return result


def returning_quantity(name):
    result = dict()
    returned_quantity = int(input("Please input the quantity to return, Enter to return: "))
    #quantity = remaining_quantity(name)
    for user, returned in user_borrow_record.items():
        if user[1] == name:
            #returned_quantity = quantity + returned_quantity
            print("User: ", user, ITEMS[1][INDEX_ITEM_TOTAL_QUANTITY])
            result[user] = returned
            new = returned - returned_quantity

    #counts = 0

    for k, i in user_borrow_record.items():
        print(f"Item(s) {user[0]} had borrowed: ")
        print("Item No. | Item Name                                   | Qty.Borrowed")
        print(f"{name:>7}. | {ITEMS[k[1]][INDEX_ITEM_NAME]:<41} |  {new:>8}")
        print(user_borrow_record)
        break
# write a function remaining_quantity which accepts one parameter(tuple item)


def remaining_quantity(item_name):
    base_quantity = ITEMS[item_name][2]
    quantity = base_quantity
    for A, B in record.items():
        if A[1] == item_name:
            quantity = quantity - B
    return quantity


def display_all():
    for k, i in user_borrow_record.items():
        print(f"Item(s) Users had borrowed: ")
        print("Item No. | Item Name                                 | Qty.Borrowed")
        print(f"{k[1]:>7}. | {ITEMS[k[1]][INDEX_USER_BORROW_RECORD]:<41} |  {i:>8}")
        print(user_borrow_record)
    return user_borrow_record


def display_user(record_name):
    check = dict()
    for k, v in user_borrow_record.items():
        if k[INDEX_USER_BORROW_RECORD] == record_name:
            check[k] = v
        else:
            print("Not valid borrower to borrow item(s)")

    #counts = 0
    for k, i in check.items():
        print(f"Item(s) {record_name} had borrowed: ")
        print("Item No. | Item Name                                 | Qty.Borrowed")
        print(f"{k[1]:>7}. | {ITEMS[k[1]][INDEX_ITEM_NAME]:<41} |  {i:>8}")
    return check


# write a function items_in_stock to display the main menu


def items_in_stock():
    print("Item(s) Borrowers had borrowed:")
    print(f"Item No. | Item Name                                  | Qty. Left")
    for A in range(len(ITEMS)):
        item = ITEMS[A][0] + " - " + ITEMS[A][1]
        print(f"{A:>7} | {item:<42} | {remaining_quantity(A):>9}")


# write a function items_borrowed which accepts one parameter(string borrower_name)
def items_borrowed(borrower_name):
    upshot = dict()
    for key, value in user_borrow_record.items():
        if key[INDEX_USER_BORROW_RECORD] == borrower_name:
            upshot[key] = value

    counts = 0
    for k, i in upshot.items():
        print(f"Item(s) {borrower_name} had borrowed: ")
        print("Item No. | Item Name                                 | Qty.Borrowed")
        print(f"{counts:>7}. | {ITEMS[k[1]][INDEX_ITEM_NAME]:<41} |  {i:>8}")
    return upshot


def main():
    # initialize global variable record
    global record
    record = dict()

    # initialize global variable user_list
    global user_list
    user_list = list()

    # initialize global variable user_borrow_record
    global user_borrow_record
    user_borrow_record = dict()

    #########################################################################################
    # replace the following code to read the list of valid borrowers from file borrowers.txt
    for line in user_list_file.readlines():
        if not line.startswith("# "):
            user_list.append(line.rstrip("\n"))
    user_list = list(filter(None, user_list))
    # end of code replacement
    ######################################################################################

    print("Welcome to Inventory Management System.")
    while True:
        # display inventory management system menu and ask for user input

        input_function = menu()

        # When user input 0 to borrow item

        if input_function == FUNCTION_BORROW_ITEM:
            # your logics for user selected borrow item function here
            items_in_stock()
            item_no = int(input("Please input the item no. to borrow (0 - 4, Enter to return) :"))
            quantity = int(input("Please input the quantity to borrow, Enter to return: "))
            name = str(input("Please input borrower's name, Enter to return: "))
            borrow_items(item_no, quantity, name)
            items_borrowed(name)
            remaining_quantity(item_no)

            # When user input 1 to return item
        elif input_function == FUNCTION_RETURN_ITEM:
            # your logics for user selected return item function here
            username = input("Please input borrower's name: ")
            returning_item(username)
            item_no = int(input("Please input the item no. to return, Enter to return: "))
            returning_quantity(item_no)

            # When user input 2 to display a particular borrower's record
        elif input_function == DISPLAY_USER_RECORDS:
            # your logics for user selected display borrower's record here
            record_name = input("Please input borrower's name, Enter to return: ")
            display_user(record_name)

            # When user input 3 to display all records

        elif input_function == DISPLAY_ALL_RECORDS:
            # your logics for user selected display all records here
            display_all()


if __name__ == "__main__":
    main()
