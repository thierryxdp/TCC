def filtraMultiplos (lista,num):
    '''recebe e retorna os números multiplos de num dentro da lista
    list, int -> int'''
    
    i = 0
    mult = []
    
    while i < len(lista):
        if int(lista[i]) % num == 0:
            list.append(mult,int(lista[i]))
        i = i + 1
    
    return mult