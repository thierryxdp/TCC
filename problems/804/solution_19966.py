#Start your python function here
def filtra_pares (notas):
    '''
    Função que recebe uma tupla de quatro elementos inteiros
    e retorna uma nova tupla contendo apenas os elementos 
    pares da tupla original
    tupla--->tupla
    '''
    if notas[0]%2==0:
        a=notas[0]
    elif notas[0]%2==1:
        a=""
    elif notas[1]%2==0:
        b=notas[1]  
    elif notas[2]%2==0:
        c=notas[2]
    elif notas[2]%2==1:
        c=""    
    elif notas[3]%2==0:
        d=notas[3] 
    elif notas[3]%2==1:
        d=""
            
    return a+b+c+d