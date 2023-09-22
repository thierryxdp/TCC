def conta_numero(numero,matriz):
    'Conta um certo numero <numero> em uma matriz e retorna a quantidade de vezes que o numero existe naquela matriz. list -> int'
    i = 0
    contador = 0
    while i <len(matriz):
        for j in matriz:
            if j = numero:
                contador = contador + 1
        i = i + 1
    return contador