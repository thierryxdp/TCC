def faltante(pecas):
    """
    Função recebe uma lista(pecas) com N-1 inteiros numerados de 1 a N e
    retorna qual número inteiro deste intervalo está faltando.
    list -> int
    """
    len(pecas)
    i=1
    while i<=len(pecas)+1:
        if i not in pecas:
            return i
        i+=1