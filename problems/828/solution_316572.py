def primo(n):
    """ verifica se o número é primo;
    int -> bool """
    ls=[]
    i=1
    for i in range(1,n+1):
        if n%i == 0:
            ls.append(i)
        i+=1
    if len(ls) < 2 or len(ls) > 2:
        return False
    else:
        return True