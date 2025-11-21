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
            add_item = input("Add Item that you want: ")
            shopping_list.append(add_item)
            # Prompt for and add an item
            pass
        elif choice == '2':
            remove_item = input("Name item you want to remove: ")
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
            else:
                print(f" This '{remove_item}' item didn't excist.")
            # Prompt for and remove an item
            pass
        elif choice == '3':
            print(f"Shopping lists:>>> {shopping_list}")
            # Display the shopping list
            pass
        elif choice == '4':
            shop = False
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()