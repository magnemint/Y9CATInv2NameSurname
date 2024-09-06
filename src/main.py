def read_file(file):
    with open(file, 'r') as file:
        entries = file.read().splitlines()

    return entries

def return_longest_and_shortest_names(file):
    entries = read_file(file)
    longest_entry = max(entries, key=len)
    shortest_entry = min(entries, key=len)
    print(f'The longest and shortest names are {longest_entry.capitalize()} and {shortest_entry.capitalize()} respectively.')

file_path = 'names.txt'
return_longest_and_shortest_names(file_path)