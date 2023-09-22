def repetidos(lista):
    '''Recebe como entrada uma lista de numeros e retorna 
    o numero de vezes que um elemento da lista e igual 
    ao elemento anterior
    list -> int'''
    
    qntd_rep=0
    i=0
    
    while i<len(lista):
        if lista[i]==lista[i+1]:
            qntd_rep=qntd_rep+1
        i=i+1
        
    return qntd_rep