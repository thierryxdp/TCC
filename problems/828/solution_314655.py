def primo(numero):
    listanum = list(range(2, numero+1))
    for n in listanum:
        new = [n for n in listanum if numero%n == 0]
        if len(new) == 2:
            return True
        else:
            return False