def soma_h(n):
    '''funcao que calcula a soma e H com duas casas decimais
    int->float'''
    h =0
    for i in range(n):
        h= h+1/(i+1)
    return round(h,2)