def qtd_divisores(x):
    '''função que recebe um número e conta quantos divisores esse mesmo número tem
    entrada da função: int
    saída da função: int '''
    if x <= 0:
        return 0
    divisores = [x]
    for i in range(1,x//2+1):
        if x % i == 0:
            divisores.append(i)
    return len(divisores)