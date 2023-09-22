def qtd_divisores(n):
    lista=list(range(1,n+1))
    l1=[]
    for c in lista:
        if n%c==0:
            list.append(l1,c)
    return len(l1)
def primo(n):
    if qtd_divisores(n)==2:
        return True
    else:
        return False