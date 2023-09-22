def pontos_por_time(lista1,lista2):
    """funcao que recebe uma lista de dois elementos, com cada elemento
sendo tambem uma lista, sendo o primeiro elemento uma lista com o time mandante e o
time visitante, e o segundo elemento uma lista com os gols do time mandante e os gols
do time visitante, respectivamente. A funcao retorna um dicionario com o mapeamento
nome do time e pontos total
list,list -> dict"""
    lista1[2][0] = lista2[2][1]
    lista1[2][1] = lista2[2][0]
    if lista1[2][0] > lista1[2][1] and lista2[2][1] > lista2[2][0]:
        return {lista1[0]: 6, lista1[1]: 0}
    if lista1[2][0] > lista1[2][1] and lista2[2][1] == lista2[2][0]:
        return {lista1[0]: 4, lista1[1]: 1}
    if (lista1[2][0] > lista1[2][1] and lista2[2][1] < lista2[2][0]) or (lista1[2][0] < lista1[2][1] and lista2[2][1] > lista2[2][0]):
        return {lista1[0]: 3, lista1[1]: 3}
    if lista1[2][0] < lista1[2][1] and lista2[2][1] == lista2[2][0]:
        return {lista1[0]: 1, lista1[1]: 4}
    if lista1[2][0] < lista1[2][1] and lista2[2][1] < lista2[2][0]:
        return {lista1[0]: 0,lista1[1]: 6}
    if lista1[2][0] == lista1[2][1] and lista2[2][1] == lista2[2][0]:
        return {lista1[0]: 2, lista1[1]: 2}