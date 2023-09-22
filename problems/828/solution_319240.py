def primo(x):
    resultado = [i for i in range(1, x+1) if x% i==0]
    if len(resultado) == 2:
        return True
    else: