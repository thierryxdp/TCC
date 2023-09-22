def qtd_divisores(n):
    '''função que retorna a quantidade de divisores da entrada n;
    int->int'''
    count=0
    for i in range(1, int(n//2+1)):
        if n % i == 0:
            count=count+2

    return count