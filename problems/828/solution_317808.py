def primo(n):
    i=2
    while i < n:
        if (n%i==0):
            i=i+1
        else:
			return n%i==0
    t=2
    while t<n:
        if (n%t!=0):
            t+=1
            return n%t==0