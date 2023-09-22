def filtra_pares(n1,n2,n3,n4):
    numeros = [n1,n2,n3,n4]
    tuple(filter(lambda i: i % 2 == 0, numeros))