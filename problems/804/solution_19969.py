#Start your python function here
def filtra_pares (notas):
    '''
    Função que recebe uma tupla de quatro elementos inteiros
    e retorna uma nova tupla contendo apenas os elementos 
    pares da tupla original
    Tuple--->tuple
    '''
    w,x,y,x=notas
    if w%2==0:
        a=w
    elif w%2==1:
        a=""
    elif x%2==0:
        b=x  
    elif x%2==1:
        b=""
    elif y%2==0:
        c=y
    elif y%2==1:
        c=""    
    elif z%2==0:
        d=z 
    elif z%2==1:
        d=""
            
    return a+b+c+d