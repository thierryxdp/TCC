def primo(n):
    i=[]
    for x in range(2,n-1):
        if n%x==0:
            list.append(i,x)
        if len(i)==1:
            return True