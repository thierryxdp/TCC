def faltante(lista):
    '''recebe uma lista com os numeros de um quebra cabeca
    e retorna o numero correspondente à peça faltante
    list->int'''
    
    pecas=len(lista)+1
    listaCompleta=list(range(1,pecas+1))
    cont=0
    while cont!=pecas:
        x=listaCompleta[cont]
        if x not in lista:
            return listaCompleta[cont]
        cont=cont+1