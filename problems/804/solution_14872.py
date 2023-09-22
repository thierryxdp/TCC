#Start your python function here
def filtra_pares(lista):
    '''Recebe uma lista de quatro números e retorna apenas os números pares.
    tuple -> tuple'''
    
    nova_lista = ()
    
    if (lista[0]%2 == 0):
        nova_lista = nova_lista +(lista[0],)
        return nova_lista
    elif (lista[1]%2 == 0):
        nova_lista = nova_lista +(lista[1],)
        return nova_lista
    elif (lista[2]%2 == 0):
        nova_lista = nova_lista +(lista[2],)
        return nova_lista
    else:
        nova_lista = nova_lista +(lista[3],)
        return nova_lista