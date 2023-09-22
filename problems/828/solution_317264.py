def primo(numero):
    """De acordo com o numero de entrada, identifique se ele é primo e retorne um valor boolenao indicando se é primo ou não"""
    divi = 0
    for primos in range(1,numero+1):
        if numero%primos==0:
            divi+=1
        if divi==2:
            return True
        else:
            return False