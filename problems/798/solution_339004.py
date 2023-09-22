def freq_palavras(frases):
    '''função em que dada uma frase retorne um dicionário onde cada palavra
    da frase de entrada seja uma chave e tenha como valor o número de vezes
    que a palavra aparece;
    str -> dict'''
    d={}
    f=frases.split()
    for n in f:
        if not n in d:
            d[n]=list.count(f,n)
    return d