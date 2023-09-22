def filtraMultiplos(lista_num,n):
    '''teste'''
    multiplos=[]
    sequencia=0

    while sequencia < len(lista_num):
        if lista_num[sequencia]%n==0:
            multiplos=multiplos+(lista_num[sequencia])
        sequencia= sequencia+1

    return multiplos