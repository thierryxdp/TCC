def freq_palavras(frases):
    """retorna um dicionário onde cada palavra da string seja uma chave e tenha
    como valor o número de vezes que a palavra aparece."""
    d={}
    l=str.split(frases,' ')
    for i in range(len(l)):
        if l[i] not in d:
            d[l[i]]=list.count(l,l[i])
    return d