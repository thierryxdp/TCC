def primo(n):
    divisores=0
    for i in range(round(n/2)):
        if n%(i+1)==0:
            divisores+=1
    return divisores>1