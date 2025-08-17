def get_book_stats(book_text):
    with open(book_text) as f:
        file_contents = f.read()
        number_words = file_contents.split()
        print("Found " + str(len(number_words)) + " total words")

from collections import Counter

def return_char_counts_all(book_text):
    with open(book_text) as f:
        letters = f.read().lower()
        counts = Counter(letters)
        # Convert counts to a list of dicts
        counts_list = [{"char": k, "num": v} for k, v in counts.items()]
        # Sort by "num" in descending order
        counts_list.sort(reverse=True, key=lambda item: item["num"])
        return counts_list