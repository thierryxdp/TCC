def filtraMultiplos(lista,n):
    '''A funcao recebe uma lista com numeros e um numero n e retorna uma lista com
os numeros da lista inicial que sao multiplos de n
list,int->list'''
    multiplos=[]
    ordem=0
    while ordem<len(lista):
        if lista[ordem]%n==0:
            list.append(multiplos,lista[ordem])
        ordem=ordem+1
    return multiplos