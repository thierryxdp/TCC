def eh_quadrada(matriz):
    matriz = []
    linha = len(matriz)
    coluna=len(matriz[0])
    for i in range(linha):
            for j in range(coluna):
                 if [i]==[j]:
                    return True
                 else:
                    return False