def qtd_divisores(n):
    """ Retorna a quantidade de divisores que um número tem 
    int -> int """
    if n<0:
        return 0
    saida = 2
    for i in range(2, abs(n)//2+1):
        if n%i==0:
            saida+=1
    return saida