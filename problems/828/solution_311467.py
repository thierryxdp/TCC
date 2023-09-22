def primo(numero):
    divisores = 0
    for indice in range(1,numero + 1):
        if numero%indice == 0 and len([indice]) == 2:
            divisores = 0 + len([indice])
            e_primo = e_primo + True
    return e_primo