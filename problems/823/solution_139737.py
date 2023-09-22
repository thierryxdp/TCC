def faltante(listaPecas):
    """ função que recebe uma lista de números e retorna o número no intervalo
    que está faltando. list --> in """
    
    peca = 1
    quantPecas = len(listaPecas) + 1
    while peca <= quantPecas:
        if peca not in listaPecas:
            return peca
        peca += 1