def maiores (lista,n):

    list.append(lista, n)
   
    list.sort(lista)
    
    lista[lista.index(media)+1:]
    
def acima_da_media(notas):
    
    media = sum(notas)/len(notas)
    
    return maiores(notas,media+0.001)