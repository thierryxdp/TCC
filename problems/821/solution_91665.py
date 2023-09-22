def fatorial(n):
    'função que recebe um número e calcula seu fatorial. int->int'
    resultado=1
    x=0
    while x<n:
        resultado=resultado*(n-x)
    	x+=1
    return resultado