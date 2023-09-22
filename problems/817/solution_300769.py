def acima_da_media(x):
    """Dado as notas dos alunos, retorna somente os alunos que ficarama cima da media"""
    a=sum(x)
    m=a/2
    list.append(x,m)
    list.sort(x)
    n=list.index(x,m)
    return x[n:]