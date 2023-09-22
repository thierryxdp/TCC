# Questão 4
def qtd_divisores (numero):
    '''Função que nos dá quantos divisores um número tem'''

    i = 1
    soma = 0
    while  i <= numero:
        if numero % i == 0:
            soma += 1
        i = i+1
    return soma