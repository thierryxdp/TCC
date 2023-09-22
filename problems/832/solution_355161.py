def eh_quadrada(matriz):
    '''eh_quadrada recebe um matriz e devolve se a mesmas é quadrada ou não, se for quadrada a retorna True e se não for retorna False.
    list-->bool'''
    if matriz==[]:
        return
    elif len(matriz)==len(matriz[0]):
        return True
    else:
        return False