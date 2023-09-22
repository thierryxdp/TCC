def faltante(listaPecas):
    """Funcao que retorna o numero da peca faltante em um quebra-cabecas dado
    	uma lista com N - 1 numeros inteiros nao repetidos de 1 a N"""
    n = len(listaPecas) + 1
    somatotal = n * (n+1)//2
    return somatotal - sum(listaPecas)