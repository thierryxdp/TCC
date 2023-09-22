def primo(n):
    i=2
    cont=0
    while i<n:
        if n%i==0:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False