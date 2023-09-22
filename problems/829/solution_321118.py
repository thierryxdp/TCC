def soma_h(N):
    '''Esta função calcula o valor de H, de acordo com a fórmula
    dada e com o número de termos (N) inserido.
    int -> float'''
    
    soma=0
    
    for numero in range(1,N+1):
        divisao=1/numero
        soma=soma+divisao
        H=round(soma,2)
        
    return H