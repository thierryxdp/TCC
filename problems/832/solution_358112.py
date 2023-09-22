def eh_quadrada(m):
    if(m==[]):
        return True
    else:
        lin=len(m)
        col=len(m[0])
        if(lin!=col):
            return False
        else:
            return True