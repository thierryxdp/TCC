def faltante (lista):
    '''
    Recebe uma lista com N-1 numeros que correspondem 
    a numeração das peças de um quebra cabeça e retorna 
    qual esta faltando
    list--->int
    '''
    listaordenada=list.sort(lista)
    posicao=0
    numero=1
    while listaordenada(posicao)==numero:
        posicao=posicao+1
        numero=numero+1
    return numero