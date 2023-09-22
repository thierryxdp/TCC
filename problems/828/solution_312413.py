def primo(numero):
    lista = list(range(numero))
    pos = 1
    if numero == 1:
        return False
    for elemento in lista:
        while numero%lista[pos] == 0:
            pos = pos + 1
    return True