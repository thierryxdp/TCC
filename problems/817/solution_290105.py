def acima_da_media(a):
    """funcao que dada uma lista com as notas dos alunos retorne as notas acima da media.
    lista->lista."""
    x=len(a)
    m=sum(a)/x
    list.append(a,m)
    list.sort(a)
    y=list.index(a,m)
    b=a[y:]
    z=list.pop(b,0)
    if z==b[1]:
        del b[1]
        return b
    else:
        return b