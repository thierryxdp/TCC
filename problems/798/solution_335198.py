def freq_palavras(frases):
    frases=frases.split(' ')
    cnt = Counter(frases)
    for Word in frases:
        cnt[Word] += 1
    return cnt