def primo(p):
    """Função que dado um número inteiro positivo, verifique se este número é primo ou não,
    int --> bool"""
    contador = 0
    for i in range(1,p+1):
        if p%i==0:
            contador = contador+1
    if contador==2:
        return True
    else:
        return False