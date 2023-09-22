def primo(x):
    lista = []
    for y in range(1, x):
        if x%y == 0:
            lista.append(y)
    if lista == [1]:
        return True
    if lista != [1]:
        return False