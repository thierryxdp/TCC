def eh_quadrada(matriz):
    numero_colunas = len(matriz)
    numero_e_linha = len(matriz[0])
    if numero_colunas == numero_e_linha:
        return True
    elif numero_colunas != numero_e_linha:
        return False