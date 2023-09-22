def soma_h(N):
    '''A função retorna a soma de N termos fracionários
    cujo numerador é sempre 1 e o denominador vai de 1
    até N. int -> int'''
    
    i = 1
    soma = 0
    
    while (1/i)<=(1/N):
        soma = soma + 1/(i)
        
        i=i+1
        
    return round(soma,2)