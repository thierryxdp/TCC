def qtd_divisores(n):
    '''Função que dado um numero inteiro n, retorna quantos divisores esse
numero tem
int -> int'''
    soma= 0
    for x in range(1,n+1):
        if n%x == 0:
            soma= soma + 1
    return soma