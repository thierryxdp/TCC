#Start your python function here
def filtra_pares(numero):
    '''Esta e a funcao que'''
    pares=numero%2
    if pares == 0:
        return numero-(numero%2!=0)
    else:
        return numero