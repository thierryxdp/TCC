def qtd_divisores(n):
    '''Retorna a quantidades de divisores de n;
    int -> list'''
    lista = []
    for i in range(1,n+1):
        if n%i == 0:
            list.append(lista, i)
            
        i = i+1
        
    return len(lista)