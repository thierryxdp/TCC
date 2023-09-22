def qtd_divisores(n):
    '''qtd_divisores recebe um numero inteiro e devolve outro numero inteiro
    determine quantos divisores o numero n possui 
    int --> int'''
    
    lista = []
    
    for numero in range(1,n+1):
        if n%numero==0:
            list.append(lista,numero)   
    
    return len(lista)