def qtd_divisores(n):
    
    numero = n
    lista = list(range(1,n+1))
    
    divisores = list(filter(lambda x: numero%x == 0, lista))
    resultado = len(divisores)
    
    return resultado