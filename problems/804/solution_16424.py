#Start your python function here
def filtragempar(numero):
    '''Esta e a funcao que'''
    impares=(numero%2!=0)
    pares=numero%2
    if pares == 0:
        return numero-impares
    else:
        return numero