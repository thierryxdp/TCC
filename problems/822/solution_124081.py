def repetidos(L):
    """Funcao que recebe como entrada uma lista L de numeros
    e retorna o numero de vezes que um elemento da lista e 
    igual ao elemento anterior;
    lista->int"""
    
    i=0
    n=0
    
    while i<len(L)-2:
        if L[i]==L[i+1]:
            n=n+1
        i=i+1
    return n