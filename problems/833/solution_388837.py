def conta_numero(numero,matriz):
    ''' funcao que dado um numero e uma matriz retorna a quantidade de vezes que esse numero aparece na matriz. int, list --> int'''
    contador = 0
    for linha in matriz:
        for coluna in linha:
            if coluna == numero:
                contador += 1
    return contador