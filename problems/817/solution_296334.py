def maioresq(lista,n):
    '''
        dada um lista e um inteiro n retorna os valores da lista maiores que n
        lista,int -> list
    '''
    copia=list.copy(lista)
    list.append(copia,n)
    list.sort(copia)
    index=list.index(copia,n)
    return copia[index+1:]

def acima_da_media(notas):
    '''
        dada uma lista de notas, faz a média entre elas e retornas os valores
        maiores que a média.
        list -> list
    '''
    media=int(sum(notas)/len(notas))
    listaM= maioresq(notas,media)
    if media in listaM:
    	list.remove(listaM,media)
    return listaM