def soma_h(n):
    '''Programa qu retorna a soma dos termos tendo n como entrada
    int -> float'''
    i = 1
    h = 0
    for i in range(1,n+1):
        h = h + 1/i
        i = i + 1
    return round(h,2)

    
soma_h(10)