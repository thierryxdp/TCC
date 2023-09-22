def freq_palavras(frases):
    dic={}
    palavras=frases.split(' ')
    for string in palavras:
        indice=palavras.count(string)
        dic[string]=indice
    return dic