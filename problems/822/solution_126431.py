def repetidos(lnumeros):
    '''Função que recebe uma lista de números lnumeros e retorna o número de vezes que um elemento;
    é igual ao elemento anterior;
    list -> str'''
    i=0
    while i<=len(lnumeros):
        if len(set(lnumeros)) != len(lnumeros):
            anterior = anterior + 1
        i+=1
    return anterior