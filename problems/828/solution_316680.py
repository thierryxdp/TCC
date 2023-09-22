def primo(n):
    indece=2
    for indece in range(1,n+1):
        if n%indece!=0:
            indece=indece+1
            return True
        else:
            indece=indece+1
            return False