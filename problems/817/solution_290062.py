def acima_da_media(a):
    """funcao que dada uma lista com as notas dos alunos retorne as notas acima da media.
    lista->lista."""
    x=len(a)
    m=sum(a)/x
    list.append(a,m)
    list.sort(a)
    x=list.index(a,m)
    b=a[x:]
    list.remove(b,m)
    return b