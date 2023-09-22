def repetidos(lista):
    "função que recebe uma lista de numeros e retorna o numero(int) de vezes que um elemento da lista se repetiu"
    posicao = 0
    lista2 = []
    list.sort(lista)
    while posicao < len(lista):
        if list.count(lista,lista[posicao]) > 1:
            while list.count(lista,lista[posicao]) > 1:
                list.remove(lista,lista[posicao])
        list.append(lista2,lista[posicao]
                    posicao +=1
            return lista2