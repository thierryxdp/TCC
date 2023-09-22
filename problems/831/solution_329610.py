def lingua_p(palavra):
    ''' recebe uma palavra e retorna essa palavra minuscula coma letra p apos cada
    vogal seguido dessa mesma vogal.
    str --> str'''
    str.lower(palavra)
    listapalavra=list(palavra)
    lista=[]
    for i in range(listapalavra):
        if listapalavra[i] in 'aeiouAEIOUáéíóúãõâêîôûÁÉÍÓÚÂÊÎÔÛÃÕ':
            list.append(lista,listapalavra[i] + 'p' + listapalavra[i])
        else:
            list.append(lista,listapalavra[i])
                
    return str.join('',lista)