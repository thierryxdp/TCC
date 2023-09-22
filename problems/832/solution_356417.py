def eh_quadrada(matriz):
    resultado=''
    if matriz==[[]]:
        return True
    for i in range(len(matriz)):
        x=range(len(matriz))
        for j in range(len(matriz[0])):
            y=range(len(matriz[0]))
            if x!=y:
                resultado=False
            if x==y:
                resultado=True
    return resultado