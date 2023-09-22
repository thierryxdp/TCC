def primo(n):
    x=[]
    for i in range(2,int(n**(1/2))):
        if n%i==0:
            x.append(i)
    if x==[]:
        return True
    else:
        return False