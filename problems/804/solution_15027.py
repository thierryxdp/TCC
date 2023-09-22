#Start your python function here
def filtra_pares(E1,E2,E3,E4):
    ''' filtra os numeros dados apresentando apenas os pares'''
    tupla= ()
    if E1%2==0:
        tupla+E1
    if E2%2==0:
        tupla+E2
    if E3%2==0:
        tupla+E3
    if E4%2==0:
        tupla+E4
    return tupla