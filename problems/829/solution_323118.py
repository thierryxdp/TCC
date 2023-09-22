def soma_h(n):
    
    contador=0
    soma=0
    
    for x in range(0,n):
        if x<n:
            contador=contador+1
            soma=soma+(1/n)+(1/(n-contador))
            
            return soma