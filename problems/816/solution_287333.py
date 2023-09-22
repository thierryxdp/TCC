#Função que recebe uma lista e um inteiro e retorna uma nova lista
#em ordem crescente apenas com os numeros maiores que o inteiro
#recebido
#list, int -> list
def maiores(lista_numeros, n):
    i = 0
    lista_atualizada = []
    while i < len(lista_numeros):
        if lista_numeros[i] > n:
        	lista_atualizada.append(lista_numeros[i])
        i += 1
    lista_atualizada.sort()
    return lista_atualizada