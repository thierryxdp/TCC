def qtd_divisores(n):
    '''função em que dado um número (n) conte quantos divisores esse número tem;
    int -> int'''
    d=0
    for i in range(1,n+1):
        if n%i==0:
            d+=1
    return d

def primo(n):
    '''função em que dado um número inteiro positivo(n) verifique se este
    número é primo ou não;
    int -> bool'''
    if qtd_divisores(n)>2:
        return False
    else: #quando ele for primo
        return True