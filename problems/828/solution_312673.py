def primo(numero):
    """Funcao que retorna de um numero é primo ou não, tendo como entrada 
    um numero inteiro."""
    if numero != 0 & numero != 1:
        if numero > 3:
            for i in range(2, numero):
                if numero % i == 0:
                    return False
        return True
    return False