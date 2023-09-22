x=(a,b,c,d)
def filtra_pares(x):
    """Recebe uma tupla com quatro elementos inteiros como entrada e retorna
       uma nova tupla contendo apenas os elementos paresda tupla original
       parãmetro de entrada: tipo tupla
       parâmetro de saída: tipo tupla"""
    return list(filter(filtra_pares,x))