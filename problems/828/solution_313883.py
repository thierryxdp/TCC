def primo(n):
    lista = []

    for i in range(n)[2:]:
        lista.append(n / i)

    for i in lista:
        if not i.is_integer():
            return False
        else:
            return True