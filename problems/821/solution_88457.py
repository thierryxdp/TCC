#Questão 5
def fatorial(num):
    """Função que dado um número, retorna o fatorial dele;
    int->int"""
    fator = 1
    while fator <= num:
        fator += 1
        multiplicacao = num
        fatorial = multiplicacao*fator
    return fatorial