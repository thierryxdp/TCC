def soma_h(x):
    """Função que calcula e retorna o valor de H com X termos onde X é inteiro e dado como entrada"""
    """int->float"""
    for y in range(x):
        if y==0:
            som=som +0
        else:
            som=som+1/y
    return round(som+1/x,2)