def primo(numero):
    """FUNÇÃO QUE RETORNA SE O NÚMERO É PRIMO OU NÃO"""
    for i in range(2,numero-1):
        if numero%i==0:
            return False
    return True