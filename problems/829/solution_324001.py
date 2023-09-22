def soma_H(n):
    """calcular e retornar o valor H com N termos, onde N  ́e inteiro
e  ́e dado como entrada.
int->int"""
    soma=0
    numeros=1
    for i in range(n+1):
        if i>=1:
            soma=soma+numeros/i
    return round(soma,2)