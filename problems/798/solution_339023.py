def freq_palavras(frases):
    ''' retorna um dicionário onde cada palavra dessa string seja uma chave e tenha como valor o número de vezes que a palavra aparece, dada uma string;
    str -> dict '''
    d = {}
    p = str.split(frases)
    for elem in p:
        x=list.count(p,elem)
        d[elem]= x
    return d