import sys
from pathlib import Path
from colorama import Fore

# Display the directory structure recursively.
def display_directory(directory: Path, depth: int = 0) -> None:
    for item in directory.iterdir():
        # Create indent to show the directory structure hierarchy.
        indent = '  ' * depth

        if item.is_dir():
            # Display the name of the directory in blue.
            print(f'{indent}{Fore.BLUE}{item.name}')

            # Process the subdirectory recursively.
            display_directory(item, depth + 1)
        else:
            # Display the name of the file in green.
            print(f'{indent}{Fore.GREEN}{item.name}')

def main() -> None:
    # Check whether directory path is given.
    if len(sys.argv) <= 1:
        print('Please add a directory path: python hw03.py <directory_path>')
        return

    # Create a path object using the directory path.
    directory = Path(sys.argv[1])

    # Check whether the directory exists.
    if not directory.exists():
        print(f'{Fore.RED}Error: The path "{directory}" does not exist.')
        return

    # Check whether the directory is a directory.
    if not directory.is_dir():
        print(f'{Fore.RED}Error: The path "{directory}" is not a directory.')
        return

     # Display the name of the root directory in blue.
    print(f'{Fore.BLUE}{directory.name}')

    # Display all files and subdirectories.
    display_directory(directory, 1)

if __name__ == "__main__":
    main()
