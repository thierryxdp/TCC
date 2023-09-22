#Start your python function here

def filtra_pares(tupla_quatro_elementos):
    """
    Essa função recebe uma tupla com quatro elementos inteiros 
    e retorna uma nova tupla contendo somente números pares, na mesma 
    ordem que estavam na tupla inicial.
    tuple -> tuple
    """
    lista = []
    for elementos in tupla_quatro_elementos:
        if elementos % 2 == 0:
            lista.append(elementos)
        tupla_resultado = tuple(lista)
    return tupla_resultado