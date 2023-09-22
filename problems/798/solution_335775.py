def freq_palavras(frases):
    """ função que recebe uma string e retorna um dicionario 
    onde cada palavra dessa string seja uma chave e tenha como 
    valor o número de vezes que ela aparece
    str->dict
    """
    freq={}
    n=0
    separados=frases.split(' ')
    for i in range(len(separados)):
        n=separados.count(separados[i])
        freq[separados[i]]=n
    return freq