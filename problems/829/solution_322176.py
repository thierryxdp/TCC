def soma_h(n):
    soma = 0
    for i in range(1,n+1):
        soma =soma + int (i)/(n-(i-1))
        return round soma