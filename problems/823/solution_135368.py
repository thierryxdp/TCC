def faltante(lista):
    '''recebe uma lista com os numeros de um quebra cabeca
    e retorna o numero correspondente à peça faltante
    list->int'''
    
    pecas=len(lista)+1
    listaCompleta=list(range(1,pecas+1))
    cont=0
    while cont!=pecas:
        if lista[cont] not in listaCompleta:
            return lista[cont]
        cont=cont+1