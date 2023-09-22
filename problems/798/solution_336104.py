def freq_palavras(frase):
    """Função que recebe uma str e retorna um dicionario
    onde cada palavra é contada
    str-->dict"""
    lista = frase.split(' ')
    dicionario = {}
    for palavra in lista:
        if palavra not in dicionario:
            dicionario[palavra]= 1
        else:
            dicionario[palavra]+=1
    return dicionario