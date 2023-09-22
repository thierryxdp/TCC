def qtddivisores(numero):
    '''Função que conta quantos divisores um numero possui,
    int -> int'''
    
    lista = []
    A = range(numero+1)
    for num in A[1:] :
        if numero % num == 0:
           lista = lista + [numero] 
    return len(lista)