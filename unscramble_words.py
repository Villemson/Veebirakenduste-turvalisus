def unscramble_words(scrambled_words, wordlist):
    unscrambled_list = []
    for word in scrambled_words:
        word = word.lower()
        for candidate in wordlist:
            candidate = candidate.lower().strip()
            if len(candidate) == len(word) and sorted(candidate) == sorted(word):
                unscrambled_list.append(candidate)
                break
        else:
            unscrambled_list.append(None)
    return unscrambled_list

wordlist_file = "wordlist.txt"

scrambled_words = input("Sisestage ja vajutage enter. ").split(",")

with open(wordlist_file, "r") as file:
    wordlist = file.readlines()

unscrambled_list = unscramble_words(scrambled_words, wordlist)
print(", ".join(unscrambled_list))
