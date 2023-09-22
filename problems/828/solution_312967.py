def primo(num):
    cont=0
    for elemento in list(range(2,num)):
        if num%elemento==0:
            cont=cont+1
    return not cont>0