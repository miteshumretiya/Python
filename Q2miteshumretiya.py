try:
    # Open file using 'with' to ensure it closes automatically
    with open('large_sample.txt', 'r') as file: 
        word_count = {}  # Use dictionary to store word frequencies
        
        for line in file:   # Read file line by line
            words = line.split()  # Split line into words
            for word in words:
                word = word.lower()  # Convert to lowercase to avoid case mismatch
                word_count[word] = word_count.get(word, 0) + 1  # Handle missing keys safely

    # Sorting words by their count in descending order
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_words:  # Printing words line by line in descending order
        print(f"{word}: {count}")

except FileNotFoundError:
    print("Error: The file does not exist.")