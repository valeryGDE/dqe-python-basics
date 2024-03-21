initial_text = ''' tHis iz your homeWork, copy these Text to variable.


 You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.


 it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.


 last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''


def whitespaces_sum(text):
    return sum(1 for char in text if char.isspace())


print("Whitespaces number:", whitespaces_sum(initial_text))


def capitalize_text(text):
    return '. '.join(sentence.strip().capitalize() for sentence in initial_text.split('.'))


def split_all_words(text):
    return text.split()


def last_words(text):
    return [el for el in split_all_words(text) if el.endswith('.')]


def make_sentence_from_last_words(text):
    return ' '.join(last_words(text)).capitalize().replace('.', '') + '.'


def unite_texts(first_text, second_text):
    return f"{first_text}{second_text}"


united_text = unite_texts(capitalize_text(initial_text), make_sentence_from_last_words(initial_text))

corrected_iz_text = united_text.replace(' iz ', ' is ')

print("Final result:", corrected_iz_text)
