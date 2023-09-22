# função filtra multiplos de um número n

def filtraMultiplos(lista_num,n):
    '''Dado uma lista de números e um número n, retorna todos os números da lista de números múltiplos do número n.
    list, int -> list'''
    lista_nova = []
    i=0
    while i < len(lista_num):
        if lista_num[i]%n == 0:
            lista_nova.append(lista_num[i])
        i+=1
    return lista_nova