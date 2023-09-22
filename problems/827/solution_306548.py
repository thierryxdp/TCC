def qtd_divisores(n):
    ''' função que mostra os divisores de um número'''
    
    lista = list(range(1, n+1))
    
    divisores = list(filter( lambda x: n%x == 0, lista))
    
    return len(divisores)