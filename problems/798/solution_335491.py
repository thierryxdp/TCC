def freq_palavras(frases):
    'dada uma frase, retorna um dicionario com a frequencia de cada palavra str -> dict'
    fraseslist = str.split(frases)
    x = 0
    y = len(fraseslist)
    frasesdict = {}
    while(x < y):
        repeticoes = fraseslist.count(fraseslist[x])
        frasesdictx = {str(fraseslist[x]):repeticoes}
        frasesdict.update(frasesdictx)
        x = x+1
    return frasesdict