def faltante(lista):
    '''recebe uma lista com os numeros de um quebra cabeca
    e retorna o numero correspondente à peça faltante
    list->int'''
    pecas=len(lista)
    #como falta uma peca o tamanho real é len+1
    tamanho=pecas+1
    contador=0
    novaLista=[]
    while contador!=tamanho:
        contador=contador+1
        novalista=novaLista+[contador]
    return novaLista