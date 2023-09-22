#Start your python function here

def filtra_pares(num1,num2,num3,num4):
    '''Recebe quatro números inteiros e devolve na mesma ordem apenas os
    inteiros pares.
    int,int,int,int -> tupla'''
    
    lista1 = (num1,num2,num3,num4)
    lista2 = sorted(filter(lambda x: x % 2 == 0, lista1))
    
    return lista2