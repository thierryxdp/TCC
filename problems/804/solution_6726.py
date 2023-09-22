def filtra_pares(tupla):
    """ função que recebe uma tupla composta por quatro elementos
        do tipo inteiro e retorna uma nova tupla contendo apenas
        os elementos pares da primeira
        tuple -> list """
    a,b,c,d = tupla
    if a % 2 == 0 and b % 2 == 0 and c % 2 == 0 and d % 2 == 0:
        return (a,b,c,d)
    if a % 2 == 0 and b % 2 == 0 and c % 2 == 0 and not d % 2 == 0: 
        return (a,b,c)
    if a % 2 == 0 and b % 2 == 0 and not c % 2 == 0 and not d % 2 == 0:
        return (a,b)
    if a % 2 == 0 and not b % 2 == 0 and not c % 2 == 0 and not d % 2 == 0:
        return (a)
    if a % 2 == 0 and b % 2 == 0 and not c % 2 == 0 and d % 2 == 0:
        return (a,b,d)
    if a % 2 == 0 and b % 2 == 0 and not c % 2 == 0 and not d % 2 == 0: 
        return (a,b)
    if a % 2 == 0 and not b % 2 == 0 and not c % 2 == 0 and not d % 2 == 0:
        return (a)
    if a % 2 == 0 and not b % 2 == 0 and c % 2 == 0 and d % 2 == 0:
        return (a,c,d)
    if a % 2 == 0 and not b % 2 == 0 and c % 2 == 0 and not d % 2 == 0: 
        return (a,c)
    if a % 2 == 0 and not b % 2 == 0 and not c % 2 == 0 and not d % 2 == 0:
        return (a)
    if not a % 2 == 0 and b % 2 == 0 and c % 2 == 0 and d % 2 == 0:
        return (b,c,d)
    if not a % 2 == 0 and b % 2 == 0 and c % 2 == 0 and not d % 2 == 0: 
        return (b,c)
    if not a % 2 == 0 and b % 2 == 0 and not c % 2 == 0 and not d % 2 == 0:
        return (b)
    if 
    
    
  
    
    
    #Start your python function here