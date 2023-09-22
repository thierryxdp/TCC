def posLetra(string, letra, numero):
    '''recebe uma string, letra e um numero indicando a ocorrência desejada da letra, e retorna em que posição da 
    string aquela ocorrência da letra está. Se existir menos ocorrências da letra do que a pedida, retorna -1.
    str, str, int -> int'''
    Lista = str.split(string, " ")
    Valor = str.index(lista[numero], letra)
    return valor