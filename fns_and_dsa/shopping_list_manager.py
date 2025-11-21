def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    shop = True
    while shop:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item = input("Enter the item to add: ")
            shopping_list.append(add_item)
            print(f"'{add_item}' is add to shopping list.\n")
            # Prompt for and add an item
            pass
        elif choice == '2':
            remove_item = input("Enter the item to remove: ")
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
                print(f"'{remove_item}' is removed from shopping list.\n")
            else:
                print(f"'{remove_item}' item didn't exist.\n")
            # Prompt for and remove an item
            pass
        elif choice == '3':
            print(f"Shopping lists:>>> {shopping_list}\n")
            # Display the shopping list
            pass
        elif choice == '4':
            shop = False
            print("Goodbye!\n")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()