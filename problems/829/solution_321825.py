def soma_h(n):
    ''' função que cálcula o valor
    H com N termos onde N é inteiro
    e dado com entrada. int -> float'''
    r=0
    for i in range (1, n+1):
        r = r + 1/i
return round(r,2)