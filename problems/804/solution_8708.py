def filtra_pares(tupla):
    """Retorna uma nova tupla somente com os números pares da tupla original
    tuple -> tuple"""
	if tupla[0] % 2 != 0:# ESTOU TRATANDO COMO LISTA POR CONTA DO ERRO DO SISTEMA
        tupla[0] = 3
    if tupla[1] % 2 != 0:
        tupla[1] = 3
    if tupla[2] % 2 != 0:
        tupla[2] = 3
    if tupla[3] % 2 != 0:
        tupla[3] = 3
    str(tupla)