def primo(n):
    indece=2  
    while indece<n:
        if n%indece!=0:
            indece=indece+1
        
        else:
            return False
    return True