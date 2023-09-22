#Questão 5
def fatorial(num):
    """Função que dado um número, retorna o fatorial dele;
    int->int"""
    fatorial = 1
    while fatorial <= num:
        multiplicacao = fatorial*num
        fatorial += 1
    return multiplicacao