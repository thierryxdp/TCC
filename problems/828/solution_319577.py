def primo(num):
    "Informa se o número é primo"
    resultado = False
    for divisores in list(range(num)):
        if divisores > 1:
            if num//divisores == 0:
                resultado = True
    return resultado