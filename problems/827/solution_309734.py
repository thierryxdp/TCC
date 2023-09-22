def qtd_divisores(n):
    """ função que conta quantos divisores um número tem
    int,int->int"""
    i=0
    for caractere in range(1,n+1):
        if n%caractere==0:
            i=i+1
     return i