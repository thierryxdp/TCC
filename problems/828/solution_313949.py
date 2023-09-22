def primo(n):
    i=[]
    for x in range(2,n-1):
        if n%x==0:
            if x==2:
                return False
            else:
            	list.append(i,x)
        if len(i)<=1:
            return True
        if len(i)>2:
            return False