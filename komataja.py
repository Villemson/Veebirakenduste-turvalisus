scrabled_words = []
print("Sisestage s]nad eraldi ridadena. Lopus tyhi rida. ")

while True:
    word = input()
    if not word:
        break
    scrabled_words.append(word.strip())
    
scrambled_words_string = ','. join(scrabled_words)

print(scrambled_words_string)