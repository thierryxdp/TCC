def acima_da_media(l):
    'recebe uma lista contendo todas as notas dos alunos, e retorna as notas que ficaram maiores que a média aritimética do todtal list->list'
    s=sum(l)
    m=(s)/len(l)
    l= l + [m]
    list.sort(l)
    p=l.index(m)
    l=l[p:]
    list.remove(l,m)
    if m==l[0]:
        return []
    else:
        return l