text = input()
dict = {}

letter_count = 0
letter_first = text[0]

check_letter = {''}

for next_letter in text:
    for l in range(len(text)):
        if (next_letter not in check_letter):
            if (next_letter == text[l]):
                letter_count += 1
    
    if (next_letter not in check_letter):
        check_letter.add(next_letter)
        dict[next_letter] =  letter_count
    
    letter_count = 0



print(dict)