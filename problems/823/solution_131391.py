def faltante(n):
    """Funcao que retorna o numero da peca faltante em um quebra-cabecas dado
    	uma lista com N - 1 numeros inteiros nao repetidos de 1 a N"""
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num