def maiores(lista, n):
    """Recebe uma lista de valores inteiros e um valor inteiro n, retornando uma nova lista
    com todos os valores maiores que n
    assinatura: list, int --> list
    testes:
    maiores([3, 4, 5], 2)==[3, 4, 5]
    maiores([2, 5, 6], 3)==[5, 6]
    """
    n=n   
    lista.append(n)
    list.sort(lista)      
    listafin = [lists for lists in lista if lists > n]
    return listafin
def acima_da_media(notas):
    """Recebe uma lista de notas e retorna uma lista ordenada com somente as notas acima da média
    assinatura: lista --> lista
    testes:
    acima_da_media([3, 4, 5])==[5]
    acima_da_media([3,6,7])==[6, 7]
    """
    return maiores(notas, sum(notas)/len(notas))