def freq_palavras(frases):
    """funcao que recebe de entrada uma string e retorna
    um dicionario onde cada palavra dessa string e uma chave
    e tem como valor o numero de vezes que a palavra aparece;
    str -> dict"""
    
    lista_de_palavras = str.split(frases)
    dicionario = {}
    for i in lista_de_palavras:
        if i in dicionario:
            dicionario[i] = dicionario[i] + 1
        if i not in dicionario:
            dicionario[i] = 1
    return dicionario