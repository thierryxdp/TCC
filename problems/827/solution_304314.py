def qtd_divisores(num):
    '''Função que recebe um número e retorna o total de divisores que este
    número tem; int -> int'''
    total = 0
    for i in range(1,num+1):
        if num % i == 0:
            total += 1
    return total