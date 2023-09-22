def repetidos(lnumeros):
    '''Função que recebe uma lista de números lnumeros e retorna o número de vezes que um elemento;
    é igual ao elemento anterior;
    list -> str'''
    i=1
    cont=0
    while i<len(lnumeros):
        if lnumeros[i]==lnumeros[i-1]:
            cont +=1
        i+=1
    return cont