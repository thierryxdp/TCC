def primo(n):
    divisores=[]
    if n==2:
        return True
    elif n%2==0:
        return False
    else:
        d=n
        while d!=0:
            if n%d==0:
                list.append(divisores,d)
                d=d-1
            else:
                d=d-1
        if len(divisores)==2:
            return True
        else:
            return False