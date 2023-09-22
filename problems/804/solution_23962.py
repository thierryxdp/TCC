def filtra_pares[(a,b,c,d)]:
    '''função que recebe uma tupla com quatro elementos e retorna uma nova tupla com os elementos pares da original'''
    if (a)%2==0 and (b)%2==0 and (c)%2==0 and (d)%2==0:
        return a,b,c,d
    elif (a)%2==0 or (b)%2==0 or (c)%2==0 or (d)%2==0:
        return a or b or c or d