def primo(nip):
    """Esta funcao dado um numero inteiro positivo, diz se ele é primo ou nao."""
    for x in range(2,nip):
        if nip % x ==0:
            return False
    else:
            return True