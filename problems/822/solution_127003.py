def repetidos(lista):
    '''Função que retorna o número de vezes que um elemento
da lista de entrada é igual ao elemento anterior;
    lista -> int'''
    proximo=0
    vezes=0
    while proximo<len(lista)-1:
        if lista[proximo+1]==lista[proximo]:
            vezes=vezes+1
        proximo=proximo+1
    return vezes