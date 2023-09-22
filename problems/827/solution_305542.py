def qtd_divisores(n):
    '''Função que dada um inteiro, retorne quantos
    divisores esse número tem.
    Entrada: int
    Saída: int'''
    d=[]
    for numero in range(1,n+1):
        D = 1
        if numero%D==0:
            d.append(numero)
        D = D + 1
    return len(d)