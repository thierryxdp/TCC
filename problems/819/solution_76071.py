def filtraMultiplos (lista,num):
    '''recebe e retorna os números multiplos de num dentro da lista
    list, int -> int'''
    
    contador = 0
    multiplos = []
    
    while contador < len(lista):
        if lista(contador)%num == 0:
            multiplos = multiplos.append(lista(contador))
        contador = contador + 1
    
    return multiplos