def soma_h(N):
    """ recebe N termos inteiros, calcula e retorna o valor de H de acordo
    com a regra progressiva dada no exercício """
    
    for i in list(range(2, N+1)):
        H += i ** -1
        
    return round(H, 2)