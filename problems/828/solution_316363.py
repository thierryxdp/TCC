def primo(numero):
    div=[]
    for c in range(1,numero+1):
        if numero%c==0:
            div=(div+[c])
            a=len(div)
            if a>2:
                return False
            else: 
                return True