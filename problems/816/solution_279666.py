#Entrada: Uma lista e um numero inteiro
#1-Analisar quais valores são maiores que um numero inteiro n
#2-Retornar outra lista com os valores da lista maiores que n
def maiores(lista:list, n:int)->list:
    """Recebe uma lista e um número inteiro n.
    retorna a lista com os valores maiores que n."""
    lista.append(n)
    list.sort(lista)
    indice=list.index(lista,n)
    return lista[indice+1:]