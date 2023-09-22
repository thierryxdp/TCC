def freq_palavras(frases):
    """Dada a frase de entrada, retorne em um dicionário quantas vezes cada palavra da frase aparece"""
    i = dict()
    frases =frases.split()
    for x in frases:
        if x not in i:
            i[x]=1
        else:
            i[x]+=1
    return i