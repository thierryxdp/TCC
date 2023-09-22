def soma_h(n):
 '''calcula e retorna o valor H com N termos, onde N  ́é inteiro e é dado
como entrada.'''
    divisor=1
    calculo=1
    for divisor in range(2,n+1):
        calculo=calculo+(1/divisor)
    return calculo