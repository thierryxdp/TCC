#a função recebe uma lista e um numero inteiro e retorna uma lista com valores maiores do que n.
#list->list
def maiores(lista,n):
    for item in lista:
        if item>n:
        	n.append(item)
    n.sort
    return(n)