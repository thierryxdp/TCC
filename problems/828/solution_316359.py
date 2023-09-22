def primo(numero):
    div=[]
    for c in range(1,numero+1):
        if numero%c==0>2:
            div=(div+[c])
            return False
        else:
            return True