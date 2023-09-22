def freq_palavras(frase):
    """A função retorna um dicionário onde cada palavra dessa string seja uma chance e tenha como
    valor o número de vezes que a palavra aparece.
    str-->dict"""
    palavras = frase.split()
    dic = {}
    i =0
    for x in palavras:
        dic[palavras[i]] = palavras.count(palavras[i])
        i +=1
    return dic