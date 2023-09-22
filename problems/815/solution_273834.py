def insere(lista_numero,n):
    '''função que alem de adicionar um numero numa lista, o põe
    em ordem crescente
    list,int--->list'''
    lista_numero.append(n)
    list.sort(lista_numero)
    
    return lista_numero