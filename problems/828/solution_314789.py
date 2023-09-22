def primo(x):
    '''
    funcao retorna se o numero x é primo ou não
    '''
    listax=[x]
    for h in range(1,x):
        if x%h==0:
            list.append(listax,h)
    if len(listax)==2:
        return True
    elif len(listax)!=2:
        return False