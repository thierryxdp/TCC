'''Função recebe número positivo e inteiro n e retorna
True, caso seja primo, e False, caso não seja primo.
int -> bool'''
def primo(n):
    contador = 0
    acumulador = []
    for numero in list(range(n)):
        if n%(n-contador) == 0:
            acumulador = acumulador + [1]
        contador = contador + 1
    if acumulador == []:
        return True
    elif len(acumulador) == 2:
        return True
    else:
        return False