def soma_h(n):
    '''função que dado um numero é feito a soma do inverso dele.
    entrada:int
    saida:float'''
    H = 0
    for i in range(1,n+1):
        H = H + 1/i
    return round(H,2)