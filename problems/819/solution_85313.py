def filtraMultiplos(lista,n):
    '''Função que filtra os múltipos,presentes em uma lista e 
    de um número n'''
    multiplo=0
    nums=[]
    while multiplo<len(lista):
        if lista[multiplo]%n==0:
            nums=nums+[lista[multiplo]]
        multiplo= multiplo+1
    return nums