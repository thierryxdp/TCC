def faltante(lista):
    '''dada uma lista(lista) de tamanho N-1, composta por numeros inteiros (nao repetidos) de 1 a N, retorna o numero intero faltante pertencente ao intervalo[1,N], nao pertencente a lista; list -> int'''
    indice = len(lista)
    list.sort(lista)
    numero = lista[0]
    indice2 = 0
    while indice > 0:
        if lista[indice2] != numero:
            return numero
        indice = indice - 1
        numero = numero + 1
        indice2 = indice2 + 1