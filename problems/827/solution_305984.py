def qtd_divisores(n):
    '''recebe um número inteiro(n) e retorna quantos divisores esse
    número tem; int -> int'''
    lista = []
    for i in range(1,n+1):
        if n%i==0:
            lista.append(i)
    return len(lista)