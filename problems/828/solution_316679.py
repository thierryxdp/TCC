def primo(n):
    indece=2
    for indece in range(1,n):
        if n%indece==0:
            indece=indece+1
            return False
        else:
            indece=indece+1
            return True