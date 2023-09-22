def fc_divisor(n,a):
    return True if n%a ==0 else False 

def qtd_divisores(n):
    divisores = list(filter(fc_divisor, n, range(1, n+1)))
    cont = len(divisores)
            
    return cont