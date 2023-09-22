def repetidos(lista):
    """ recebe uma 'lista' de npumeros e retorna o número de vezes que um elemento
    da lista é igual ao elemento anterior.
    list -> int """
    soma = 0
    i = 0
    
    while i<len(lista):
        if lista[i]==lista[i-1]:
            soma = soma+1
        i= i+1
        
    return soma