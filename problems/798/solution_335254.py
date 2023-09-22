def freq_palavras(frases):
    """ Recebe uma string e retorna um dicionário onde cada palavra dessa string seja uma chave 
    e tenha como valor o número de vezes que a palavra aparece 
    str -> dict """
    saida = {}
    for palavra in frases.split():
        if palavra in saida.keys():
            saida[palavra]+=1
        else:
            saida[palavra]=1
    return saida