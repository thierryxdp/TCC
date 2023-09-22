def primo(numero: int):
    for n in range(1,numero+1):
        if n==numero or n==1:
            if numero%n==0:
                return True
        else:
            return False