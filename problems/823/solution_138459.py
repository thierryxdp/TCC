def faltante(lista):
    '''Funcao que analisa a lista e retorna o numero inteiro
    do intervalo dessa lista que esta faltando
    Parametro:
    list
    Saida: int
    '''
    
    h=0
    i=h+1
    while h<len(lista):
        if list[i]-list[h]==1:
            h= h+1
    return