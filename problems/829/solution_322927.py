def soma_h(N):
    '''Entrada: N -> quantidade de termos da função H, dado do tipo
    				int
       
       Saída: H -> função definida por '1+1/2+1/3+1/4+...+1/N', dado
       			   do tipo float 
    
       int -> float'''
    H = 0
    for x in range(1,N+1):
        H = H + 1/x
    return round(H,2)