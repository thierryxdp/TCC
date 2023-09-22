def primo(numero):
    """"""
    primou=0
    for numero > 0:
        if numero%2 == 0 or numero%3 == 0:
            primou=True
        else:
            primou=False
    return primou