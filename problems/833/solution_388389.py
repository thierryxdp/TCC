def conta_numero(numero, matriz):
    """Recebe um número e uma matriz e retorna a quantidade de vezes 
    que esse número aparece na matriz.
    assinatura: int, list --> int
    testes:
    """
    qtde = 0
    for a in len(matriz):
        for b in matriz[a]:
            if b == [numero]:
                qtde += 1
    return qtde