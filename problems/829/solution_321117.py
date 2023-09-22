def soma_h(N):
    '''Esta função calcula o valor de H, de acordo com a fórmula
    dada e com o número de termos (N) inserido.
    int -> float'''
    
    soma=0
    
    for numero in range(1,N+1):
        soma=soma+numero
        H=1/soma
        H2=round(H,2)
        
    return H2