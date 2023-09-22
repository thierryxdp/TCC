def eh_quadrada(matriz):
        qtd_linhas = len(matriz)
        qtd_colunas = len(matriz[0])
        if qtd_linhas == qtd_colunas:
            return True
        else:
            return False