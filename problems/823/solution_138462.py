def faltante(lista):
    '''Funcao que analisa a lista e retorna o numero inteiro
    do intervalo dessa lista que esta faltando
    Parametro:
    list
    Saida: int
    '''
    r=1
    h=0
    i= lista[h]
    j=h+1
    k=lista[j]
    while h<len(lista):
        if k-i==2:
            r=r+ k-1
        h=h+1
        
    return k