def primo(n):
    Nprimos=0
    for c in range(2,n):
        if n % c == 0:
            Nprimos+=1
    if Nprimos==0:
        return True
    else:
        return False