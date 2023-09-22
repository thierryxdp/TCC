def faltante(L):
    """Função que dada uma lista L com números inteiros
    retorna o faltante do intervalo de 1 até o maior deles
    list -> int"""
    L.sort()
    extencao = len(L)
    contador = 0
    numero = 1
    while contador < extencao:
        if numero not in L:
            return numero
        numero += 1
        contador += 1