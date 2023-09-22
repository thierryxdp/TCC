def conta_numero(numero, matriz):
    """Com um contador inicial. A função lê a matriz
    e checa se existe um dos elementos pedidos nas
    listas. Caso exista ela entra na conta e retorna
    a soma."""
    c = 0
    for x in matriz:
        c += x.count(n)
    return k