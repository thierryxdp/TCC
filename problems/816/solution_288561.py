def maiores(lista,n):
    '''dada uma lista de números inteiro e um númeroa interio n, retorna todos os números da lista original maiores que n e em ordem crescente'''
    listafinal=[ ]
    for elemento in lista:
        if elemento>n:
             return listafinal.append(elemento)