def conta_numero(numero, matriz):
    '''retorna a quantidade de vezes que um número é
    encontrado numa matriz
    int, list -> int'''
    count = []
    for lin in matriz:
        for num in lin:
            if num == numero:
                count.append(num)
    return len(count)