def repetidos(lista):
    '''Função que dada uma lista de números inteiros, retorna o número de vezes que um elemento é igual ao anterior
    list[int,...] -> int'''
    i=0
    contador=0
    while i<len(lista)-1:
        if lista[i]==lista[i+1]:
            contador+=1
        i+=1
    return contador