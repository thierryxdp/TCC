def repetidos(lista):
    ''' 
       função que recebe uma lista de numeros e retorna o 
       numero de vezes que um elemento da lista é igual ao
       elemento anterior
       list -> int
    '''
    i = 0
    soma = 0
    while i<(len(lista)-1):
        if lista[i] == lista[i+1]:
            soma=soma+1
        i=i+1
    return soma