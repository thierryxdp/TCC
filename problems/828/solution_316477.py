def primo(n):
     divisores=0
    for i in range(n+1):
        if n%(i+1)==0:
            divisores+=1
    if divisores==1:
        return True
    else: 
        return False