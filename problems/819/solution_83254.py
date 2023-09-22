def filtraMultiplos(listaN,n):
    '''Dados uma lista de números e um número n, retorna uma lista com apenas os multiplos de n contido na lista de entrada
    list,int->list'''
    multiplos=[]
    i=0
    while i<len(listaN):
        if (listaN[i]) % n==0:
            multiplos=multiplos+listaN[i]
            i=i+1
    return multiplos