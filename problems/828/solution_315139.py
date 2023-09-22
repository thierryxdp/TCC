def primo(numero):
    """Dado um número qualquer, retorna se ele é primo ou não:
    int-->bool"""
    for primo in [2,3,5,7]:
        print(numero/primo)
        if (numero%primo==0) and primo!=numero:
            return False
    return True