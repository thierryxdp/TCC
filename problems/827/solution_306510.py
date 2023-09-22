def qtd_divisores(n):
    
    numero = n
    lista = list(range(1,n+1))
    
    resultado = list(filter(lambda x: numero%x == 0, lista))
    
    return resultado