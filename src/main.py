import matplotlib.pyplot as plt

def read_file(file):
    with open(file, 'r') as f:
        entries = f.read().splitlines()
    return entries

def return_longest_and_shortest_names(file):
    entries = read_file(file)
    longest_entry = max(entries, key=len)
    shortest_entry = min(entries, key=len)
    return f'The longest and shortest names are {longest_entry.capitalize()} and {shortest_entry.capitalize()} respectively.'

def process_name(name):
    name = name.lower()
    if len(name) > 0:
        pairs = [(name[i], name[i + 1]) for i in range(len(name) - 1)]
        start_letter = name[0]
        end_letter = name[-1]
    else:
        pairs = []
        start_letter = ''
        end_letter = ''
    return {
        "pairs": pairs,
        "start_letter": start_letter,
        "end_letter": end_letter
    }

def count_from_names(names):
    pair_counts = {}
    start_counts = {}
    end_counts = {}

    for name in names:
        processed = process_name(name)
        for pair in processed['pairs']:
            if pair in pair_counts:
                pair_counts[pair] += 1
            else:
                pair_counts[pair] = 1
        start_letter = processed['start_letter']
        if start_letter:
            if start_letter in start_counts:
                start_counts[start_letter] += 1
            else:
                start_counts[start_letter] = 1
        end_letter = processed['end_letter']
        if end_letter:
            if end_letter in end_counts:
                end_counts[end_letter] += 1
            else:
                end_counts[end_letter] = 1
    return pair_counts, start_counts, end_counts

def write_pair_freqs_to_file(pair_counts, filename='pair_freqs_raw.txt'):
    sorted_pairs = sorted(pair_counts.items(), key=lambda x: x[1], reverse=True)
    with open(filename, 'w') as f:
        for pair, count in sorted_pairs:
            f.write(f"{pair}: {count}\n")

def write_sorted_pairs_to_file(pair_counts, filename='pair_freqs_sorted.txt'):
    sorted_by_first = sorted(pair_counts.items(), key=lambda x: x[0][0])
    with open(filename, 'w') as f:
        for pair, count in sorted_by_first:
            f.write(f"{pair}: {count}\n")

def plot_pair_frequencies(sorted_pairs):
    pairs, counts = zip(*sorted_pairs)
    labels = [f"{p[0]}-{p[1]}" for p in pairs]
    plt.figure(figsize=(14, 10))
    plt.bar(labels, counts, color='skyblue')
    plt.xlabel('Letter Pairs')
    plt.ylabel('Frequency')
    plt.title('Frequency of Letter Pairs')
    plt.xticks(rotation=90, ha='right')
    plt.grid(axis='y')
    plt.tight_layout(pad=2.0)
    plt.savefig('pairs_histogram.png')
    plt.show()

def filter_pairs_by_starting_letter(letter, pair_counts):
    return [(pair, count) for pair, count in pair_counts.items() if pair[0] == letter]

file_path = 'names.txt'
names = read_file(file_path)
pair_counts, start_counts, end_counts = count_from_names(names)
write_pair_freqs_to_file(pair_counts)
write_sorted_pairs_to_file(pair_counts)
sorted_pairs = sorted(pair_counts.items(), key=lambda x: x[1], reverse=True)
plot_pair_frequencies(sorted_pairs)
filtered_pairs = filter_pairs_by_starting_letter('a', pair_counts)
print(filtered_pairs)
print(return_longest_and_shortest_names(file_path))
