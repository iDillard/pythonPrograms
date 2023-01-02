#
# Isaiah Dillard
# Trish's Bookstore Inventory System
#
import pickle


# Review the main() function to see what code needs to be added. Do not change
# any other code within main().
def main():
    inventory_counts, inventory_costs = read_inventory_file()
    print("Welcome to Trish's Inventory Input System")
    print("Current Inventory:")
    display_all_inventory(inventory_counts, inventory_costs)

    response = ''
    while response != '0':
        # Display the user menu
        print("What would you like to do?")
        print("(1) Add an item\n"
              "(2) Display an item\n"
              "(3) Delete an item\n"
              "(4) Display all inventory\n"
              "(0) Exit")

        response = input('Enter your choice: ')
        if response == "1":  # Add an item
            item_name, item_count, unit_cost = get_item_input()

            # Create the dictionary to add the items into
            inventory_costs[item_name] = unit_cost
            inventory_counts[item_name] = item_count
            print(f'{item_name} added to inventory')
            print()

        # Option to display an item
        elif response == "2":
            item_name = input('Enter item name: ')
            if item_name in inventory_counts:
                print(f'{item_name}, Count: {inventory_counts[item_name]}, Cost: {inventory_costs[item_name]}')
                print()
            else:
                print('item not found')
                print()

        # Option to Delete an item
        elif response == "3":  # Delete an item
            item_name = input('Enter item name: ')
            inventory_counts.pop(item_name)
            inventory_costs.pop(item_name)
            print(f'{item_name} Deleted')
            print()

        # Display the inventory

        elif response == "4":  # Display all inventory
            display_all_inventory(inventory_counts, inventory_costs)
        elif response != "0":
            print("Invalid choice. Try again.\n")
            print()

    display_all_inventory(inventory_counts, inventory_costs)

    save_inventory_file(inventory_counts, inventory_costs)


def display_all_inventory(inventory_counts, inventory_costs):
    # This function will display the items in the inventory and the respective cost
    if len(inventory_counts) and len(inventory_costs) != 0:
        print(f'Item count: {inventory_counts}')
        print(f'Item price: {inventory_costs}')
    else:
        print('---Empty---')


def save_inventory_file(inventory_counts, inventory_costs):
    # this function will use the pickle module to save to a binary file

    inventory_file = open('inventory.dat', 'wb')
    pickle.dump(inventory_counts, inventory_file)
    pickle.dump(inventory_costs, inventory_file)
    inventory_file.close()
    print('inventory.dat file was created')
    print()
    pass


def read_inventory_file():
    # This function will look for an existing inventory file
    # If an existing file is not found display nothing will happen

    inventory_counts = {}
    inventory_costs = {}
    try:
        inventory_file = open('inventory.dat', 'rb')
        inventory_counts.update(pickle.load(inventory_file))
        inventory_costs.update(pickle.load(inventory_file))
    except FileNotFoundError:
        pass
    return inventory_counts, inventory_costs


def get_item_input():
    # Get item name
    while True:
        item_name = input('Enter the item name: ')
        if ',' in item_name:
            print('Item names cannot contain commas.')
        else:
            break
    # Get item count
    while True:
        try:
            item_count = int(input('Enter the item count: '))
            if item_count < 0:
                print('Item count must be 0 or greater.')
            else:
                break
        except:
            print('Item count must be an integer.')
    # Get unit cost
    while True:
        try:
            unit_cost = float(input('Enter the unit cost: '))
            if unit_cost < 0:
                print('Unit cost must be 0 or greater.')
            else:
                break
        except:
            print('Unit cost must be an integer.')
    return item_name, item_count, unit_cost


main()
