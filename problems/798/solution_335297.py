def freq_palavras(frases):
    '''
       funcao que recebe uma string e retorna um dicionario 
       onde cada palavra dessa string é uma chave e tem como
       valor o numero de vezes que a palavra aparece
       str -> dict
    '''
    lista = frases.split()
    dicio = {}
    for el in lista:
        dicio.update({el:lista.count(el)})
    return dicio