def primo(numero):
    e_primo = 0
    for indice in range(1,numero + 1):
        if numero%indice == 0 and len([indice]) == 2:
            e_primo = e_primo + True
    return e_primo