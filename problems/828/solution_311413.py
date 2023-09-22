def primo(n):
    i=0
    for numero in range(2,n):
        if (n%numero==0):
            return('',numero)
        i+=1
    if(i==0):
        return('')
    else:
        return('',i,'',n)