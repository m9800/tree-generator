# Path to the text file containing file paths
path_to_text_file = "scope.txt"

# Read file paths from the text file
with open(path_to_text_file, "r") as file:
    files = [line.strip() for line in file.readlines()]

# Function to insert files into the tree
def insert_into_tree(tree, path):
    current_node = tree
    for part in path:
        if part not in current_node:
            current_node[part] = {}
        current_node = current_node[part]

# Function to print the tree
def print_tree(tree, indentation="", is_last=True):
    keys = list(tree.keys())
    for i, key in enumerate(keys):
        prefix = "└── " if i == len(keys) - 1 else "├── "
        print(f"{indentation}{prefix}{key}")
        if tree[key]:  # If the item has subitems
            new_indentation = indentation + ("    " if i == len(keys) - 1 else "│   ")
            print_tree(tree[key], new_indentation, i == len(keys) - 1)

# Create the tree structure
directory_tree = {}
for file in files:
    path_parts = file.split("/")[1:]  # Ignoring the first element (repository name)
    insert_into_tree(directory_tree, path_parts)

# Print the tree
print("contracts")
print_tree(directory_tree["contracts"], is_last=False)

