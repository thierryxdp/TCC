def qtd_divisores(n):
    '''funcao que dado um numero retorna a quantidade de numeros divisores inteiros do numero atribuido.int/float->int'''
    divisores = 0
    for i in range(1,n + 1):
        if n % i==0:
            divisores +=1
    return divisores