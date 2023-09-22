def soma_h(n):
    '''Função que calcula e retorna o total H com n termos onde n é inteiro e dado como entrada.
    int -> float'''
    x = 0
    for H in range(1,n+1):
        x  += (1/(H))
    return round (x,2)