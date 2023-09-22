def repetidos(lista=[]):
    '''Recebe como entrada uma lista de numeros e retorna
    o numero de vezes que um elemento da lista é igual ao 
    elemento anterior'''
    '''list->int'''
    cont=0
    for i in range(len(lista)):
        if i>0 and lista[i]==lista[i-1]:
            cont+=1
    return cont