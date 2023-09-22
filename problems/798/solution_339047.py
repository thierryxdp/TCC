def freq_palavras(frases):
    wordlist = wordstring.split()
    wordfreq = []
    for w in wordlist:
        wordfreq.append(wordlist.count(w))

        
    return dict(list(zip(wordlist,wordfreq)))