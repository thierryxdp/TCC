def eh_quadrada (matriz: list) -> bool:
    """Recebe uma matriz qualquer e retorna True se ela é quadrada, False
    caso contrário."""
    if len(matriz) > 0:
    	numero_de_linhas = len(matriz)
        numero_de_colunas = len(matriz[0])
        if numero_de_linhas == numero_de_colunas:
            return True
        else:
            return False
        
    else: #matriz vazia, é considerada uma matriz quadrada
        return True