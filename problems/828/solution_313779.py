def primo(n):
    """ Função que retorna se o número é primo(True)
    ou se não é primo(False).
    Entrada: int
    Saída: bool """
    for d in range(2,n):
        if n%d==0:
            return False
    return True