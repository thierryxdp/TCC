def freq_palavras(frases):
    frases = wordstring.split()
    wordfreq = []
    for w in wordlist:
        wordfreq.append(wordlist.count(w))

        
    return dict(list(zip(frases,wordfreq)))