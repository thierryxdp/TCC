def fatorial (numero):
    """ função que dado um número ela calcula o fatorial deste número 
    fatorial é o produto do número  (N)x(N-1)x(N-2) ... até chegar no número 1
    exemplo : fatorial de 3 = 3x2x1=6
    fatorial de 4 =4x3x2x1=24
    entrada-> int
    retorna-> int"""
    
    repeticoes=1
    resposta=1
    
    while repeticoes==numero:
        resposta= resposta*repeticoes
        repeticoes=  repeticoes+1
        
    return resposta