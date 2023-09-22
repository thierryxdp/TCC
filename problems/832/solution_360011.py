def eh_quadrada(matriz):
    "Função que recebe uma matriz e retorna True se ela for quadrada."
    "list -> bool"
    a = len(matriz)
    if a == 0:
        return True
    if len(matriz[0]) == a:
        return True
    else:
        return False