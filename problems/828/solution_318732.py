def primo(n):

    cont=0
    for c in range(1,n+1):
        if n%c==0:
            cont +=1
        if cont == 2:
            return True
        elif cont > 2:
            return False