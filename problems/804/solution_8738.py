#Start your python function here
def filtra_pares(lista):
    '''Recebe uma lista de quatro números e retorna apenas os números pares.
    tuple -> tuple'''
    
    nova_lista = ()
    
    if (lista[0]%2 == 0):
        nova_lista = nova_lista +(lista[0],)
    if (lista[1]%2 == 0):
        nova_lista = nova_lista +(lista[1],)
    if (lista[2]%2 == 0):
        nova_lista = nova_lista +(lista[2],)
    if (lista[3]%2 == 0):
        nova_lista = nova_lista +(lista[3],)
    return nova_lista#Start your python function here