def insere(lista_numero,n):
    '''função que dada uma lista ordenada(crescente) inclua n na posiçãocorreta:list,int:list'''
    if n in lista_numero: 
        return list.sort(lista_numero)
    else:
        list.append (lista_numero, n)
        list.sort(lista_numero)
        return lista_numero