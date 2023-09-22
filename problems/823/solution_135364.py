def faltante(lista):
    '''recebe uma lista com os numeros de um quebra cabeca
    e retorna o numero correspondente à peça faltante
    list->int'''
    
    pecas=len(lista)+1
    listaCompleta=list(range(1,pecas))
    return listaCompleta