def eh_quadrada(matriz):
    """Função que retorna se uma função é quadrada ou não. Entrada: Lista. Saida: strig"""
    nlin = range(len(matriz))
    ncol = range(len(matriz[0]))
    if nlin==[]:
        Matriz ='True'
    if nlin == ncol:
        Matriz= 'True'
    if nlin != ncol:
        Matriz ='False'
    return Matriz