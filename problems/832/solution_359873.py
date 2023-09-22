def eh_quadrado(matriz):
    if len(matriz) == 0:
        return True
    elif len(matriz) == 2:
        for i in matriz:
            if len(i) == 2:
                return True
            else: 
                return False