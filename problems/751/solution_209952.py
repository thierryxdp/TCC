def quant_palavras(frase):
    '''funcao que diz quantas palavras tem em uma frase;
str -> int'''
    lista = str.split(str.strip(frase))
    quantidade = len(lista)
    return quantidade