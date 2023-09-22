def qtd_divisores(n):
    """Retorna quantas divisões um numero tem. int -> int"""
    lista = []
    for a in range(1,n+1): 
        if n%a == 0: 
            list.append(lista,a)
    return len(lista)