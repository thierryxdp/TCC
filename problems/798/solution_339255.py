def freq_palavras(frase):
    '''Função que dada uma string e um dicionário, retorna a quantidade
de vezes que a palavra aparece.
list -> dici'''
    dicio = {}
    lista = str.split(frase)
    for palavra in lista:
        if palavra in dicio:
            dicio[palavra] = dicio[palavra] + 1
        else:
            dicio[palavra] = 1
    return dicio