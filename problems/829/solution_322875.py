def soma_h(n):
    'dada a expressão H, retorne a soma dos termos até o numero n.int-->float'
    soma=0
    for i in range(1,n+1):
        soma=soma +1/i
    return round(soma,2)