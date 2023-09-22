#Questão 5
def fatorial(num):
    """Função que dado um número, retorna o fatorial dele;
    int->int"""
    fator = 1
    multiplicacao = 1
    while fator < num:
        fator += 1
        multiplicacao = multiplicacao*fator
    return multiplicacao