def soma_h(N):
    """calcular e retornar o valor H com N termos,
onde N é inteiro e é dado como entrada"""
    i = 0 
    n = list(range(1,N+1))#abreviando
    H = 0
    
    while i < len(list(range(1,N+1))):
        H += 1/n[i] #soma as divisões

        i += 1

    return round(H,2)