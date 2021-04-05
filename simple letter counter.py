text = input()
dict = {}

for char in text:
    dict[char] = text.count(char)
    
print(dict)