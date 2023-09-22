def substitui(s,x,i):
    """Calcule e retorne uma palavra s que tenha o caractere i substituído por um caractere x escolhido"""
    if i <= len(s):
        return str(s)[0:i] + str(x) + str(s) [i:]
    else:
        return