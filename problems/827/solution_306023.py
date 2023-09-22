def qtd_divisores(x):
    '''Função que recebe um número e conta quantos divisores ele tem.
    entrada da função: int
    saída da função: int'''
    divisores = [x]
    for i in range(1, x//2+1):
        if x % i == 0:
            divisores.append(i) 
    return len(divisores)