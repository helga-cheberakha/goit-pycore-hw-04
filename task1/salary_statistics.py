# Read the file and return its content as a list of lines.
def load_data(filepath: str) -> list[str]:
    with open(filepath, 'r', encoding='utf-8') as file:
        return [el.strip() for el in file.readlines()]

# Clean the data and return a list of valid salaries.
def clean_data(employees: list[str]) -> list[float]:
    employee_salaries = []

    for employee in employees:
        # Skip empty row.
        if not employee:
            continue

        # Split row using "," as a separator
        employee_data = [value.strip() for value in employee.split(',')]

        # Skip row without a salary or with empty salary.
        if len(employee_data) != 2 or not employee_data[1]:
            print(f'Warning: Invalid number of columns in row "{employee}".')
            continue

        # Convert salary from a string to a digit.
        try:
            employee_salary = float(employee_data[1])
        except ValueError:
            print(f'Warning: Invalid salary "{employee_data[1]}" in row "{employee}".')
            continue

        employee_salaries.append(employee_salary)

    return employee_salaries


# Calculate the total and average salaries.
def calculate_salary(salaries: list[float]) -> tuple[float, float]:
    if not salaries:
        return 0.0, 0.0

    total_salary = sum(salaries)
    average_salary = total_salary / len(salaries)

    return total_salary, average_salary

# Get the total and the average salaries.
def total_salary(filepath: str) -> tuple[float, float]:
    try:
        employees = load_data(filepath)
        salaries = clean_data(employees)

        return calculate_salary(salaries)
    except FileNotFoundError:
        print(f'The file "{filepath}" does not exist.')
        return 0.0, 0.0
        

total, average = total_salary('./../files/documents/salary_file.txt')
print(f"Загальна сума заробітної плати: {total:.2f}, Середня заробітна плата: {average:.2f}")

total, average = total_salary('/wrong_path_to_file.txt')
print(f"Загальна сума заробітної плати: {total:.2f}, Середня заробітна плата: {average:.2f}")
