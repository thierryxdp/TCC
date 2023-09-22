def primo(numero):
    contador=0
    for i in range(numero):
        if numero%(i+1)==0:
            contador=contador+1
    if contador==2:
        return True
    else:
        return False