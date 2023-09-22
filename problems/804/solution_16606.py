#Start your python function here
def filtra_pares(numero):
    '''Esta e a funcao que recebe uma tupla com quatro
    elementos inteiros e retorna uma nova tupla contendo 
    apenas os elementos pares da tupla original'''
    n1 = numero[0]
    n2 = numero[1]
    n3 = numero[2]
    n4 = numero[3]
    if n1%2!=0 and n2%2!=0 and n3%2!=0 and n4%2==0:
        return (n4,)
    elif n1%2!=0 and n2%2!=0 and n3%2==0:
        return (n3,)
    elif n1%2!=0 and n2%2==0:
        return (n2,)
    elif elif n1%2==0 and n4%2==0:
        return (n1,n4)
    elif n1%2==0:
        return (n1,)
    else:
        return ()