def primo(numero):
    """A funcao primo recebe como entr"""
    divisores = 0
    for indice in range(1,numero + 1):
        if numero%indice == 0:
           divisores = divisores + len([indice])
    return bool(divisores == 2)