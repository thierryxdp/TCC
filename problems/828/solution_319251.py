def primo(n):
    x=[]
    i=2
    while i in range(2,n):
        if n % i==0:
            x.append(i)
        i+=1
    if x==[]:
        return True
    else:
        return False