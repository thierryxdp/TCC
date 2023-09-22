def soma_h(n):
    '''
    Função que calcula e retorna o valor H com N termos na expressão:
    
    H=1+ 1/2 + 1/2 + 1/3 + ..... + 1/N
    
    Dado o numero N
    
    int---> float
    '''
    d=n
    r=0
    while d!=0:
        r+=1/d
        d-=1
    return round(r,2)