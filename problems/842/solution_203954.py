def pontos_por_time(lista):
    """funcao que recebe uma lista de dois elementos, com cada elemento
sendo tambem uma lista, sendo o primeiro elemento uma lista com o time mandante e o
time visitante, e o segundo elemento uma lista com os gols do time mandante e os gols
do time visitante, respectivamente. A funcao retorna um dicionario com o mapeamento
nome do time e pontos total
list,list -> dict"""
    if lista[0][2][0] > lista[0][2][1] and lista[1][2][1] > lista[1][2][0]:
        return {lista[0][0]: 6, lista[0][1]: 0}
    if lista[0][2][0] > lista[0][2][1] and lista[1][2][1] == lista[1][2][0]:
        return {lista[0][0]: 4, lista[0][1]: 1}
    if (lista[0][2][0] > lista[0][2][1] and lista[1][2][1] < lista[1][2][0]) or (lista[0][2][0] < lista[0][2][1] and lista[1][2][1] > lista[1][2][0]):
        return {lista[0][0]: 3, lista[0][1]: 3}
    if lista[0][2][0] < lista[0][2][1] and lista[1][2][1] == lista[1][2][0]:
        return {lista[0][0]: 1, lista[0][1]: 4}
    if lista[0][2][0] < lista[0][2][1] and lista[1][2][1] < lista[1][2][0]:
        return {lista[0][0]: 0,lista[0][1]: 6}
    if lista[0][2][0] == lista[0][2][1] and lista[1][2][1] == lista[1][2][0]:
        return {lista[0][0]: 2, lista[0][1]: 2}