def filtra_pares(tupla):
    """Função que recebe uma tupla com quatro elementos inteiros
    e retorna uma nova tupla"""
    pares = []
    for element in tupla:
        if element %2==0:
            pares.append(element)
            return Tuple(pares)