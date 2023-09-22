def qtd_divisores(n):
    ´'''Dado um número n, retorna a quantidade de
divisores de n. int-> int'''
    total=0
    for i in range(n):
        if n%i==0:
            total+=1
    return total