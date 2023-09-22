def substitui(s,x,i):
    """Calcule e retorne uma palavra s que tenha o caractere i substituído por um caractere x escolhido"""
    if i == 4:
        return str(s)[0:3] + "x" + str(s)[5:]
    else:
        return