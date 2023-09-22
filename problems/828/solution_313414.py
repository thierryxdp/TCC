def primo(numero):
    """"""
    
    
    while 0 < numero:
        if numero == 1 or numero%3 == 0 or numero%numero:
            return True
        else:
            return False