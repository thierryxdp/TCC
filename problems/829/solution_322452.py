def soma_h(n):
    '''função que retorna o valor de uma soma com n termos onde N é inteiro e dado como entrada;int->float'''
    h=0
    for i in list(range(1,n+1)):
        h=h+1/i
    return round(h,2)