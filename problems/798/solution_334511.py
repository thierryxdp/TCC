def freq_palavras(string):
    '''Conta o número de vezes que cada palavra aparece
       em uma string;
       str -> dict'''
    palavras = {}
    lista_palavras = str.split(string)
    for palavra in lista_palavras:
        if palavra not in dict.keys(palavras):
            palavras[palavra] = list.count(lista_palavras, palavra)
    return palavras