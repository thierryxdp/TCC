def soma_h(n):
    """função que recebe um numero inteiro (n) e retorna o valor
    H com n termos
    int->float
    """
    soma=0
    numeros=1
    for i in range(n+1):
        if i>=1:
            soma=soma+numeros/i
    return round(soma,2)