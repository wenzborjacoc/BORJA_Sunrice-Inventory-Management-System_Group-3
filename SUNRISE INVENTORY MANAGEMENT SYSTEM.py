# Inventory Management System for Rice Sacks
# This program manages an inventory of rice types, tracking quantity and reorder levels.

inventory = []  # List of dictionaries, each representing a rice product

def display_menu():
    """Displays the main menu options."""
    print("\nInventory Management System")
    print("+----+------------------------------------+")
    print("| No |              Action                |")
    print("+----+------------------------------------+")
    print("| 1  | Add Product (Sack of Rice)         |")
    print("| 2  | Update Product                     |")
    print("| 3  | Delete Product                     |")
    print("| 4  | Search Product                     |")
    print("| 5  | View All Products                  |")
    print("| 6  | Exit                               |")
    print("+----+------------------------------------+")

def get_positive_integer(prompt, min_value=1):
    """Prompts for a positive integer input, with validation."""
    while True:
        try:
            value = int(input(prompt))
            if value < min_value:
                if min_value == 1:
                    print("1 is the minimum value allowed.")
                else:
                    print(f"Please enter a number greater than or equal to {min_value}.")
            else:
                return value
        except ValueError:
            print("Please enter a valid integer.")

def add_product():
    """Adds a new rice product to the inventory."""
    name = input("Enter rice type: ").strip()
    if not name:
        print("Rice type cannot be empty.")
        return
    
    # Check if rice type already exists
    for item in inventory:
        if item['name'].lower() == name.lower():
            print(f"Rice type '{name}' already exists. Use update option to modify.")
            return
    
    quantity = get_positive_integer("Enter quantity in sacks: ")
    reorder = get_positive_integer("Enter reorder level in sacks: ")
    
    inventory.append({'name': name, 'quantity': quantity, 'reorder': reorder})
    print(f"Added {quantity} sacks of '{name}'.")

def display_inventory():
    """Displays the current inventory in a table format."""
    if not inventory:
        print("No products in inventory.")
        return
    
    print("\nCurrent Inventory:")
    print("+------------------+----------------+----------------------+")
    print("| Rice Type        | Quantity       | Reorder Level        |")
    print("+------------------+----------------+----------------------+")
    for item in inventory:
        print(f"| {item['name']:<16} | {item['quantity']:<14} | {item['reorder']:<20} |")
    print("+------------------+----------------+----------------------+")

def update_product():
    """Updates an existing rice product's quantity and reorder level."""
    if not inventory:
        print("No products in inventory.")
        return
    
    display_inventory()
    name = input("Enter rice type to update: ").strip()
    
    for item in inventory:
        if item['name'].lower() == name.lower():
            new_quantity = get_positive_integer("Enter new quantity in sacks: ")
            new_reorder = get_positive_integer("Enter new reorder level in sacks: ")
            
            item['quantity'] = new_quantity
            item['reorder'] = new_reorder
            print(f"'{item['name']}' updated successfully!")
            return
    
    print("Rice type not found.")

def delete_product():
    """Deletes a rice product from the inventory."""
    if not inventory:
        print("No products to delete.")
        return
    
    display_inventory()
    name = input("Enter rice type to delete: ").strip()
    
    for item in inventory:
        if item['name'].lower() == name.lower():
            inventory.remove(item)
            print(f"🗑️ Deleted '{item['name']}'.")
            return
    
    print("Rice type not found.")

def search_product():
    """Searches for a specific rice product by name."""
    name = input("Enter rice type to search: ").strip()
    
    for item in inventory:
        if item['name'].lower() == name.lower():
            print(f"Found: {item['name']} - Quantity: {item['quantity']} sacks, Reorder Level: {item['reorder']} sacks")
            return
    
    print("Product not found.")

def view_all_products():
    """Displays all products in the inventory."""
    if not inventory:
        print("No products in inventory.")
        return
    
    print("\nInventory Report:")
    print("+------------------+----------------+----------------------+")
    print("| Rice Type        | Quantity       | Reorder Level        |")
    print("+------------------+----------------+----------------------+")
    for item in inventory:
        print(f"| {item['name']:<16} | {item['quantity']:<14} | {item['reorder']:<20} |")
    print("+------------------+----------------+----------------------+")

def main():
    """Main function to run the inventory management system."""
    while True:
        display_menu()
        choice = input("Select an option (1-6): ").strip()
        
        if choice == '1':
            add_product()
        elif choice == '2':
            update_product()
        elif choice == '3':
            delete_product()
        elif choice == '4':
            search_product()
        elif choice == '5':
            view_all_products()
        elif choice == '6':
            print("Exiting the Inventory Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
