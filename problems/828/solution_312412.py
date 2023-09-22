def primo(numero):
    lista = list(range(numero))
    pos = 3
    if numero == 1:
        return False
    for elemento in lista:
        if numero/1 == numero and numero/numero == 1 and numero%lista[pos] != 0:
            pos = pos + 1
            return True
        else:
            return False