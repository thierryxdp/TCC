def primo(n):
    '''int->bool'''
    list(range(1,n+1))
    lista=[]
    i=1
    for i in list(range(1,n+1)):
        if n%i==0:
            list.append(lista,i)
            i=i+1
    if len(lista)==2:
        return True
    else:
        return False