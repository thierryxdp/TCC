def filtraMultiplos(lista,n):
    '''função que recebe como entrada uma lista de numeros inteiros e
    como outra entrada um número n, retornando uma lista contendo todos
    os elementos da lista de entrada que são divisíveis por n;
    list,int->list'''
    
    i=0
    final=[]
    
    while i<len(lista):
        if lista[i] % n == 0:
            final= final + [lista[i]]
        i=i+1
    return final