def insere(lista_numero,n):
    '''adiciona o número n na lista lista_numero de forma que a lista continue crescente
    	list,int->list'''
    
    lista_nova=lista_numero + [n]
    lista_nova.sort()
    
    return lista_nova