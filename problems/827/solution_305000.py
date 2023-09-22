def fc_divisor(a):
    return True if int(a) == a else False 

def qtd_divisores(n):
    listanumeros = list(range(1,n+1))
    divisores = [n/numero for numero in listanumeros]
    divisores = list(filter(fc_divisor, divisores))
    cont = len(divisores)
            
    return cont