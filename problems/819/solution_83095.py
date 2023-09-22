def filtraMultiplos(lista,n):
    '''Função que recebe uma lista e um inteiro e retorna uma lista com apenas os múltiplos do número recebido
    list, int -> list'''
    nova=[]
    i=0
    while lista[i]<len(lista):
        if lista[i]%n==0:
            list.append(nova,lista[i])
        i=i+1
    return nova