def faltante(lista):
    "função que recebe uma lista de inteiros consecutivos e retorna o inteiro que está faltando"
    list.sort(lista)
    posicao = 0
    lista2 = list(range(max(lista)+1))
    if lista == lista2:
        return max(lista) + 1
    else:
        while lista[posicao] == lista2[posicao]:
            posicao += 1
        return posicao + 2