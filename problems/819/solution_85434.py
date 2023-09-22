def filtraMultiplos(lista,numero):
    '''Filtra os múltipos de n presentes em uma lista.
    list, int -> list'''
    n=0
    nums=[]
    while n<len(lista):
        
        if lista[n] % numero == 0:
            list.append(nums,lista[n])
        n=n+1
    return nums