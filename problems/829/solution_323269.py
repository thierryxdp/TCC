def soma_h(n:int)->float:
    '''retorna a soma de (1/1)+(1/2)+(1/3)...até (1/n) com duas casas decimais'''
    i=0
    a=0
    while i+1<n:
        a+=1/i+1
    i+=1
    return a