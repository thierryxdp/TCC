def qtd_divisores(n):
    """Calcula e retorna quantos divisores o número n tem.
    int --> int"""
    
    lista_divisores = []
    
    for i in range(1,n+1):
        if n%i == 0:
            list.append(lista_divisores, i)
        return len(lista_divisores)