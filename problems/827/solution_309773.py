def qnt_divisores(num):
    '''funcao que recebe um numero e retorna o numero de divisores que ele tem
    int -> int'''
    i=0
    total=0
    while i<=num:
        if num%i==0:
        	total=total+1
        i=i+1
    return total