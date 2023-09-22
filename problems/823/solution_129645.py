def faltante(pecas):
    """Função para determinar qual peça de um quebra-cabeça está faltando.
       Onde: "pecas" é uma lista com a númeração de todas as peças do quebra-cabeça (exceto a que está faltando).
    list --> int """
    n = 0
    while n < len(pecas):
        if pecas[n] != n + 1:
            return n + 1
        n += 1
    return n + 1