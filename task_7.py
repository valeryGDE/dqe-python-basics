import csv
import re


def word_count(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
        words = re.findall(r'\b[\w/.]+\b', text.lower())

    word_count = len(words)
    with open('word_count.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Word_count'])
        writer.writerow([word_count])


def letter_analysis(file_path):
    with open(file_path, 'r') as f:
        text = f.read()

    letter_dict = {}
    for letter in text:
        if letter.isalpha():
            letter_lower = letter.lower()
            if letter_lower not in letter_dict:
                letter_dict[letter_lower] = {'count_all': 0, 'count_uppercase': 0}
            letter_dict[letter_lower]['count_all'] += 1
            if letter.isupper():
                letter_dict[letter_lower]['count_uppercase'] += 1

    with open('letter_analysis.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Letter', 'Count_all', 'Count_uppercase', 'Percentage'])
        for letter, counts in letter_dict.items():
            percentage = (counts['count_uppercase'] / counts['count_all']) * 100
            writer.writerow([letter, counts['count_all'], counts['count_uppercase'], f'{percentage:.2f}%'])
