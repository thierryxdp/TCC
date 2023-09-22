#Start your python function here
def filtra_pares(tupla: tuple) ->tuple:
    
    nova_tupla = []
    
    for numero in tupla:
        if numero % 2 == 0:
            nova_tupla.append(numero)
    return tuple(nova_tupla)