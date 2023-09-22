def filtraMultiplos(lista,n):
    
    '''Função que recebe uma lista de números e verifica quais desses são múltiplos de um outro número de entrada, retornando uma lista com os que satisfazem essa condição. list,int -> list'''
    
    i = 0
    multiplos = []

    while i < len(lista):
        if (lista[i]%n == 0):
            multiplos = multiplos + [lista[i]]
        i = i + 1
    
    return multiplos