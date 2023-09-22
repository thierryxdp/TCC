#Start your python function here
def filtra_pares(numero):
    '''Esta e a funcao que'''
    if numero[0]%2 and numero[1]%2 and numero[2]%2 and numero[3]%2==0:
        return numero[0:]
    elif numero[0]%2 and numero[1]%2 and numero[2]%2==0:
        return numero [:3]
    elif numero[0]%2 and numero[1]%2==0:
        return numero [:2]
    else:
        return ()