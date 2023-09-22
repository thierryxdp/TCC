def fatorial(n):
    m=1
    resultado=1
    while m<n:
        if m==1:
            multiplicacao=m*n
        else:
            multiplicacao=m
        
        resultado=multiplicacao*resultado
        m=m+1
    return resultado