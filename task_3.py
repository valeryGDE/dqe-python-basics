initial_text = ''' tHis iz your homeWork, copy these Text to variable.


 You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.


 it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.


 last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''

whitespaces_sum = sum(1 for char in initial_text if char.isspace())

print("Whitespaces number:", whitespaces_sum)

capitalized_text = '. '.join(sentence.strip().capitalize() for sentence in initial_text.split('.'))

all_words = initial_text.split()

last_words = [el for el in all_words if el.endswith('.')]

sentence_from_last_words = ' '.join(last_words).capitalize().replace('.', '') + '.'

united_text = f"{capitalized_text}{sentence_from_last_words}"

corrected_iz_text = united_text.replace(' iz ', ' is ')

print("Final result:", corrected_iz_text)
