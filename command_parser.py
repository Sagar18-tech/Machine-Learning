import os
import subprocess

def create_file(filename):
    """Creates a new empty file."""
    if os.path.exists(filename):
        print(f"File '{filename}' already exists.")
    else:
        with open(filename, 'w') as f:
            pass
        print(f"File '{filename}' created successfully.")

def open_file(filename):
    """Opens an existing file using the default program."""
    if os.path.exists(filename):
        os.startfile(filename)
        print(f"Opening '{filename}'...")
    else:
        print(f"File '{filename}' not found.")

def search_file(filename, start_dir="."):
    """Searches for a file by name in the given directory."""
    print(f"Searching for '{filename}'...")
    found = False
    for root, dirs, files in os.walk(start_dir):
        if filename in files:
            print("Found:", os.path.join(root, filename))
            found = True
    if not found:
        print("No file found with that name.")

def rename_file(oldname, newname):
    """Renames a file."""
    if os.path.exists(oldname):
        os.rename(oldname, newname)
        print(f"Renamed '{oldname}' → '{newname}'")
    else:
        print(f"File '{oldname}' not found.")

def delete_file(filename):
    """Deletes a file."""
    if os.path.exists(filename):
        confirm = input(f"Are you sure you want to delete '{filename}'? (y/n): ")
        if confirm.lower() == 'y':
            os.remove(filename)
            print(f"File '{filename}' deleted.")
        else:
            print("Operation cancelled.")
    else:
        print(f"File '{filename}' not found.")


# --- COMMAND DISPATCHER ---
commands = {
    "create": create_file,
    "open": open_file,
    "search": search_file,
    "rename": rename_file,
    "delete": delete_file
}


# --- MAIN LOOP ---
def main():
    print("Simple File Command System (Windows)")
    print("Supported commands: create, open, search, rename, delete")
    print("Example: 'create file test.txt' or 'rename file old.txt new.txt'\n")

    while True:
        user_input = input(">>> ").strip().lower()
        if user_input in ['exit', 'quit']:
            print("Exiting system.")
            break

        tokens = user_input.split()

        if len(tokens) < 3:
            print("Invalid command format.")
            continue

        action, obj = tokens[0], tokens[1]

        if obj != "file":
            print("Only 'file' operations are supported right now.")
            continue

        if action not in commands:
            print("Unknown command. Try: create, open, search, rename, delete.")
            continue

        # handle multi-argument commands like rename
        if action == "rename":
            if len(tokens) < 4:
                print("Usage: rename file oldname newname")
                continue
            oldname, newname = tokens[2], tokens[3]
            commands[action](oldname, newname)
        elif action == "search":
            filename = tokens[2]
            commands[action](filename, start_dir=".")
        else:
            filename = tokens[2]
            commands[action](filename)


if __name__ == "__main__":
    main()
