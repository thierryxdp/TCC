def filtraMultiplos (lista,num):
    '''recebe e retorna os números multiplos de num dentro da lista
    list, int -> int'''
    
    i = 0
    multiplos = []
    
    while i < len(lista):
        if lista[i] % num == 0:
            multiplos = multiplos + lista[i]
        contador = contador + 1
    
    return multiplos