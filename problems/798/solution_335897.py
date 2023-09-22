def freq_palavras(frase):
    '''Dada uma frase, retorna um dicionário onde cada
    palavra dessa frase é uma chave e tem como valor o
    número de vezes que a palavra aparece.
    str -> dict'''
    dicionario = {}
    lista_frase = frase.split()
    for palavra in lista_frase:
        dicionario[palavra]=frase.count(palavra)
    return dicionario