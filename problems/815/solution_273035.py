def eh_ordenada(lista):
    '''Função que,dada uma lista não vazia com uma quantidade qualquer de valores
    numericos, diz se a lista está ordenada em ordem crescente,decrescente ou não ordenada.
    list-->tup(bool,str)'''
    lista1 =lista[:]
    lista2 = lista[:]
    list.sort(lista1)
    list.sort(lista2,reverse = True)
    if lista == lista1:
        return True,'crescente'
    if lista == lista2 :
        return True,'decrescente'
    else :
        return False,'desordenada'