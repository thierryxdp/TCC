def qtd_divisores (n):
    """Função que informa quantos divisores o número "n" fornecido tem."""
    """int--int"""
    lista=list(range(1,n+1))
    divisores=[]
    for elemento in lista:
        if n%elemento==0:
            list.append(divisores,elemento)
    return len(divisores)