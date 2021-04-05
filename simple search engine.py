text = input()
word = input()

def search(text, word):
    if word in text:
        print('Word found')
    else: 
        print('Word not found')

search(text, word)