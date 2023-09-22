def qtd_divisores(num):
    """ recebe um numero e retorna quantos divisores ele tem"""
    c=0
    
    for i in range(1,num+1):
        if num%i == 0:
            c = c+1
    return c