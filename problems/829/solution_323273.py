def soma_h(n:int)->float:
    '''retorna a soma de (1/1)+(1/2)+(1/3)...até (1/n) com duas casas decimais'''
    i=1
    a=0
    while i<=n:
        a+=1/i
        i+=1
    return a