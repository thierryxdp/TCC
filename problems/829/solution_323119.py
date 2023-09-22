def soma_h(n):
    
    contador=0
    soma=1
    
    for x in range(1,n):
        if x<n:
            contador=contador+1
            soma=soma+(1/n)+(1/(n-contador))
            
            return soma