def soma_h(n):
    '''Função que calcula e retorna o valor de H, sendo esta uma expressão matemática
dada pela soma: 1+1/2+1/3+1/4...+1/N
    int -> float
    '''
    soma = 0
    for a in range(1,n+1):
        soma += 1/range(n+1)[a]
    return round(soma,2)