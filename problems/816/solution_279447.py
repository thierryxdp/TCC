def maiores(lista,n):
    """ insere o número n em uma lista,coloca a em ordem a nova lista e, por fim, retorna 
    uma nova lista com valorer maiores que n;list,int->list"""
    lista1=lista+[n]
    list.sort(lista1)
    return lista1[(len(n)+1):]