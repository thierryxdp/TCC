def primo(numero):
    """jhh"""
    contagem=0
    for item in range(1,numero+1):
        if numero%item ==0:
            contagem+=1
    if contagem >=2:
        return False
    else:
        return True