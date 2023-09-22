def faltante(lista):
    '''Funcao que analisa a lista e retorna o numero inteiro
    do intervalo dessa lista que esta faltando
    Parametro:
    list
    Saida: int
    '''
    n= len(lista)
    h=1
    i=0
    if lista[0] !=1:
        return 1
    while i<n:
        if h<lista[i]:
            return lista[i]+1
        if h== lista[i]:
            h+=1
            i+=1
        else:
            i==n
            return h