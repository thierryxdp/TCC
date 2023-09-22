def acima_da_media(x):
    """Dado as notas dos alunos, retorna somente os alunos que ficarama cima da media"""
    a=sum(x)
    d=len(x)
    m=a/d
    list.append(x,m)
    list.sort(x)
    n=list.index(x,m)
    list.remove(x,m)
    return x[-n:]