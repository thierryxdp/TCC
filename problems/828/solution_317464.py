def primo(numero):
    x=0
    for i in numero:
        if numero%i==0:
            x=x+1
        return x==2