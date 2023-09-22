def primo(num):
    ''' '''
    r=list(range(1,(num+1)))
    lista=[]
    for i in r:
        if (num%i)==0:
            lista=lista+[i]
    if len(lista)<=2:
        return True
    else:
        return False