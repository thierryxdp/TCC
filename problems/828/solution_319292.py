def primo(numero):
    if numero % 2 == 0 and numero % 3 == 0 and numero % 5 == 0 and numero % 7 == 0 and numero % 11 == 0:
        return 'False'
    elif numero % numero == 0:
        return 'True'