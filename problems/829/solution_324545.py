def soma_h(N):
    """ dado um numero de termos de H, retornas o valor da soma de H.
    entrada inteiro -> saida float"""
    
    d = list(range(1, N+1))
    H = 0
    
    for proximo in d:
        H = H + (1/proximo)
    return round(H,2)