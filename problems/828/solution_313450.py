def primo(numero):
    """"""
    primou=0
    for numero >= 2:
        if numero or numero%3 == 0:
            primou=True
        else:
            primou=False
    return primou