def primo(n):
    div=[]
	for i in range(n+1):
        if i!=0 and n%i==0:
	        div=div+[i]
    return len(div)==2