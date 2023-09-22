def eh_quadrada(matriz):
    """Retorna um valor booleano caso uma 
    matriz seja quadrada.
    caso a matriz seja vazia tambem sera
    considerada quadrada.
    list -> bool"""
    for i in range(len(matriz)):
        if len(matriz) == len(matriz[i]):
            return True
        elif len(matriz) == 0:
            return True
        else:
            return False