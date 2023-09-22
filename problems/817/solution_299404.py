def acima_da_media(lista_numero):
    '''Dado uma lista de notas, retornará as melhores notas acima da média
     entre elas, em uma lista ordenada.(lista=>lista)''' 
    n = sum(lista_numero) // len(lista_numero)+1
    melhores = maiores(lista_numero, n)

    return melhores