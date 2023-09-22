def freq_palavras(frases):
    wordlist = wordstring.split()
    wordfreq = []
    for w in wordlist:
        wordfreq.append(wordlist.count(w))
        print("String\n" + wordstring +"\n")
        print("Lista\n" + str(wordlist) + "\n")
        print("Frequências\n" + str(wordfreq) + "\n")
        print("Pares\n" + str(list(zip(wordlist, wordfreq))))
        
    return dict(list(zip(wordlist,wordfreq)))