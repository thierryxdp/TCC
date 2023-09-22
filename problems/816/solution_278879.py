'''Recebe uma lista de numeros inteiros e retorna outra lista apenas daqueles que sao maiores que um valor inteiro n'''
#list, int -> list
def maiores_que(numeros, n):
    list.append(numeros, n)
    list.sort(numeros)
    indice = list.index(numeros, n)
    return numeros[indice + 1:]