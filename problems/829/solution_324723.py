def soma_h(N):
    '''A função calcula o valor H de uma soma de
    N termos onde cada fração tem o denominador 
    igual a sua posição na soma.
    int --> float'''
    
    listasoma = [1]
    
    for numero in range(2,N+1):
        listasoma.append((numero)**-1)
        
    soma = sum(listasoma)
    
    return round(soma, 2)