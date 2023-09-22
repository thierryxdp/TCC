def faltante (lista_num):
    """função que recebe um lista numérica qualquer (lista_num)
    e verifica qual número que está faltanto desse intervalo. E por
    fim retorna o número que falta <n>, tal que o primeiro índice seja
    igual a 1;
    lista->int"""
    n = 1
    while n in lista_num:
        n = n + 1
    return n