#a função retorna uma lista com as notas que ficaram acima da média.
#list->list
def maiores(lista,n):
    z=[]
    for item in lista:
        if item>n:
        	z.append(item)
    z.sort()
    return(z)
def acima_da_media(lista):
    n=sum(lista)/len(lista)
    lista.maiores(lista,n)