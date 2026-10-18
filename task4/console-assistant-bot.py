# Parse the user input and split it into command
# and arguments.
def parse_input(user_input: str) -> tuple:
    # Split user input into command and arguments.
    user_input_parts = user_input.split()

    if not user_input_parts:
        return '', []

    cmd, *args = user_input_parts
    cmd = cmd.strip().lower()
    return cmd, *args

# Add the contact name and phone number.
def add_contact(args: list, contacts: dict) -> str:
    # Validate the user input. It should include
    # a name and a phone number.
    if len(args) != 2:
        return 'Input is incorrect. It should include a contact name as a first argument, and a phone number as a second argument.'

    name, phone = args

    # Check whether a contact with the given name
    # already exists.
    if get_contact_by_name(name, contacts):
        return f'Contact "{name}" already exists.'

    contacts[name] = phone
    return 'Contact has been added.'

# Update the phone number of the contact.
def change_contact(args: list, contacts: dict) -> str:
    # Validate the user input. It should include
    # a name and a phone number.
    if len(args) != 2:
        return 'Input is incorrect. It should include the existing contact name as a first argument, and a new phone number as a second argument.'

    name, phone = args

    # Check whether a contact with the given name exists.       
    contact = get_contact_by_name(name, contacts)
    if not contact:
        return f'Contact with the "{name}" does not exist.'

    contacts[contact[0]] = phone
    return 'Contact has been updated.'

# Display the phone number of the contact.
def display_contact_phone(args: list, contacts: dict) -> str:
    # Validate the user input. It should include a name.
    if len(args) < 1:
        return 'Please enter the contact name.'

    name = args[0]

    # Check whether a contact with the given name exists.  
    contact = get_contact_by_name(name, contacts)
    if not contact:
        return f'Contact with the "{name}" does not exist.'
    
    return f'Contact "{name}" has phone number {contact[1]}.'

# Display all existing contacts.
def display_all_contacts(contacts: dict) -> str:
    if not contacts:
        return 'No contacts found.'

    return '\n'.join(f'{name}: {phone}' for name, phone in contacts.items())

# Find contact by their name.
def get_contact_by_name(name: str, contacts: dict) -> tuple | None:
    for contact_name, contact_phone in contacts.items():
        if contact_name.casefold() == name.casefold():
            return contact_name, contact_phone

    return None

def main():
    contacts = {}

    print('Welcome to the assistant bot!')
    
    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)

        if not command:
            print('Please enter a command.')
            continue

        if command in ['close', 'exit']:
            print('Good bye!')
            break

        elif command == 'hello':
            print('How can I help you?')

        elif command == 'add':
            print(add_contact(args, contacts))

        elif command == 'change':
            print(change_contact(args, contacts))

        elif command == 'phone':
            print(display_contact_phone(args, contacts))

        elif command == 'all':
            print(display_all_contacts(contacts))

        else:
            print('Invalid command.')

if __name__ == "__main__":
    main()
