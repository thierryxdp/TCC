def qtd_divisores(n):
    '''funcao q conta quants divisores um numero tem'''
    '''int -> int'''
    soma = 0
    
    for d in range(1,num+1):
        if num % d == 0:
            soma = soma + 1
    return soma