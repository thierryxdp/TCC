def freq_palavras(frases):
    """retorna um dicionario com o nuemero de vezes que uma palavra apareceu na frase"""
    """str -> dict"""
    
    dicionario = {}
    lista = str.split(frases)
    for palavra in lista:
        dicionario[palavra] = list.count(lista,palavra)
    return dicionario