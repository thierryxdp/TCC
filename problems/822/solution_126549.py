def repetidos(numeros):
    '''Esta e a funcao que recebe uma lista de numeros
    inteiros e retorna o numero de vezes que um elemento da 
    lista e igual ao elemento anterior'''
    j=1
    vezes=0
    while j<len(numeros):
       if numeros[j]==numeros[j-1]:
           vezes= vezes+1
       j=j+1
    return vezes