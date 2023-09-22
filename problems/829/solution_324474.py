def soma_h(N):    
    'função que recebe N (número inteiro) e calcula o valor de H conforme fórmula'
    'int->int'
    soma=0
    n=1
    while n<=N:
        soma+=1/n
        n+=1
    return round(soma,2)