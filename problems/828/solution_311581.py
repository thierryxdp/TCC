def primo(n):
    """funcao que diz se um numero é primo ou nao"""
    lista=[]
    for x in range(1,n+1):
        if n%x==0:
            list.append(lista,x)
    if len(lista)==2:
        return "True"
    else:
        return "False"