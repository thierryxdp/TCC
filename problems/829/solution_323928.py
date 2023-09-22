def soma_h(n):
    '''
    função que calcula e retorna o valor H com n termos onde N é inteiro e dado como entrada;
    int -> float
    '''
    h = 0
    for num in range(1,n+1):
        h = h + 1/num
    return round(h,2)