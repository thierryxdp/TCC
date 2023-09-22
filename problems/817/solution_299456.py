#a função retorna uma lista com as notas que ficaram acima da média.
#list->list
def acima_da_media(lista):
    media=sum(lista)/len(lista)
    z=[]
    for item in lista:
        if item>media:
        	z.append(item)
    z.sort()
    return(z)