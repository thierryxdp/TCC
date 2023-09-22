def qtd_divisores(n):
    d = 0
    if(n>0):
        for i in range(1, 10000):
            if(n%i == 0):
                d+=1
        return d
    else:
        return 0
    
def primo(n):
    return qtd_divisores(n)==2