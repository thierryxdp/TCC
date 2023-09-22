#a função recebe uma lista e um numero inteiro e retorna uma lista com valores maiores do que n.
#list->list
def maiores(lista,n):
    z=[]
    for item in lista:
        if item>n:
        	z.append(item)
    z.sort
    return(z)