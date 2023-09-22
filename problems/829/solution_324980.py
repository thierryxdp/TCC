def soma_h(n):

    ''' funcao dado um numero calcula e retorna o valor de H com 

    int -> float'''

    contador = 1

    soma = 0

    while n >= contador:

        soma += 1 / contador

        contador += 1

    return round(soma, 2)