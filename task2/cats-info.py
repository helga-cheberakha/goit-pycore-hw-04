# Read the file and return its content as a list of lines.
def load_data(filepath: str) -> list[str]:
    with open(filepath, 'r', encoding='utf-8') as file:
        return [el.strip() for el in file.readlines()]

# Clean the data and return a list of valid cat records.
def clean_data(cats: list[str]) -> list[dict]:
    cats_info = []

    for cat in cats:
        # Skip empty row.
        if not cat:
            continue

        # Process the row and add valid cat information
        # to the list.
        if cat_info := process_cat_info(cat):
            cats_info.append(cat_info)

    return cats_info

# Process a row and return cat information as a dictionary.
def process_cat_info(cat: str) -> dict | None:
    # Split row using "," as a separator.
    cat_data = [value.strip() for value in cat.split(',')]
    # Return only not empty values.
    cat_data = [value for value in cat_data if value]

    # Each row must contain exactly three non-empty fields:
    # 1. id (string).
    # 2. name (string).
    # 3. age (integer).
    if len(cat_data) != 3:
        print(f'Warning: Missing or empty required fields in row "{cat}".')
        return None

    # Validate that the age can be converted to an integer.
    try:
        cat_age = int(cat_data[2])
    except ValueError:
        print(f'Warning: Invalid cat age "{cat_data[2]}" in row "{cat}".')
        return None

    # Build a dictionary with the cat information.
    return {
        'id': cat_data[0],
        'name': cat_data[1],
        'age': cat_age,
    }


# Read and process cat information from the file.
def get_cats_info(filepath: str) -> list[dict]:
    try:
        cats = load_data(filepath)
        return clean_data(cats)
    except FileNotFoundError:
        print(f'The file "{filepath}" does not exist.')
        return []
        

cats_info = get_cats_info('./../files/documents/cats.txt')
print(cats_info)

cats_info = get_cats_info('/wrong_path_to_file.txt')
print(cats_info)
