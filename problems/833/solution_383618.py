def conta_numero(numero,matriz):
    """Conta e retorna quantas vezes o número aparece na matriz
       int, list --> int"""
    contador = 0
    
    for i in matriz:
        for j in i:
            if j == numero:
                contador += 1
    return contador