def soma_h(n):
    '''Função que retorna um valor H com N termos onde N
    é inteiro e dado como entrada.
    int -> float'''
    
    h = 0 
    for i in range(1, n+1):
        h = h + 1/i
        return h, 2