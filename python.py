import re
from collections import Counter
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return filtered_words
def count_word_frequency(words):
    word_counts = Counter(words)
    return word_counts
def main():
    with open("paragraphs.txt", "r") as file:
        text = file.read()
    cleaned_words = remove_stopwords(text)
    word_frequency = count_word_frequency(cleaned_words)
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")
if __name__ == "__main__":
    main()
