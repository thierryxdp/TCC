def filtraMultiplos(lista,n):
    "funcao que recebe como entrada uma lista de numeros e um numero. depois retoma outra lista que contem todoso os elemnetos da lista original"
    l = []
    proximo = 0
    while proximo  < len(lista):
        if lista[proximo] % n == 0:
            l = l +[lista [proximo],]
        proximo = proximo + 1
    return l