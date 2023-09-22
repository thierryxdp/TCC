def eh_quadrada (matriz):
    'Dada uma matriz, retorna True se a matriz for quadrada ou False caso não seja uma matriz quadrada. Entrada: list[list]. Saída: bool.'
    linhas=len(matriz)
    colunas=len(matriz[0])
    if linhas==colunas:
        return True
    elif matriz==[]:
        return True
    else:
        return False