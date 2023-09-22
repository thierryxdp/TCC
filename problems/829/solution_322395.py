def soma_h(x):
    """Função que calcula e retorna o valor de H com X termos onde X é inteiro e dado como entrada"""
    """int->float"""
    s=0
    for y in range(x):
        if y==0:
            s=s +0
        else:
            s=s+1/y
    return round(s+1/x,2)