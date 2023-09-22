'''Resolução com while'''
def primo(numero):
    divisores = 0
    contador = 0

    while contador <= numero:
        if contador > 0:
            if numero % contador == 0:
                divisores += 1
        contador += 1

    if divisores == 2:
        return True
    else:
        return False