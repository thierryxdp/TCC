def faltante(lista):
    '''Retorna o numero que falta dentro da lista;
    list->int'''
    
    list.sort(lista)
    ultimo_i=lista[-1]+2
    lista_completa=list(range(1,ultimo_i))
    i=0
    
    while i<len(lista_completa):
        if lista_completa[i] in lista:
            i+=1
        elif lista_completa[i] not in lista:
            return lista_completa[i]