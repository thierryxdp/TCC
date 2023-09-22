def faltante(lista):
    '''Funcao que analisa a lista e retorna o numero inteiro
    do intervalo dessa lista que esta faltando
    Parametro:
    list
    Saida: int
    '''
    n= len(lista)+1
    h=1
    i=0
    while i<n:
        if h== lista[i]:
            h=h+1
            i=i+1
        return h