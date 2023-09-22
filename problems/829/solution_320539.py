def soma_h(n):
    soma=0
    
    for numero in range(1, n+1):
        divisao=1/numero
        soma=soma+divisao
    return round(soma,2)