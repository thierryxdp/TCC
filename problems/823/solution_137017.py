def faltante(lista):
    "função que recebe uma lista de inteiros consecutivos e retorna o inteiro que está faltando"
    list.sort(lista)
    posicao = 0
    while posicao < len(lista):
        if not lista[posicao] + 1 == lista[posicao+1]:
    posicao += 1
            return lista[posicao]+1