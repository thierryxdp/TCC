def primo(int_pos):
    lista = []
    for x in range(2,int_pos):
        if int_pos % x == 0:
            lista.append(x)
    if len(x) == 0:
        return True
    else:
        return False