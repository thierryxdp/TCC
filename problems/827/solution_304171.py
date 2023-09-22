def qtd_divisores(n):
    '''dado um numero inteiro n, retorna a quantidade de divisores que o mesmo possui
    entrada: int
    saida:int'''
    qnt=0
    for i in range(n):
        if n%i==0:
            qnt=qnt+1
    return qnt