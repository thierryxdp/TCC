def soma_h(n):
    '''
    função que calcula e retorna o valor H com n termos onde N é inteiro e dado como entrada;
    int -> float
    '''
    h = 0
    for num in range(n):
        h = h + 1/n
    return round(h,2)