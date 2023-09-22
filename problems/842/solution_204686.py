def pontos_por_time(l):
    '''Dada uma lista de 2 elementos, onde cada elemento também é uma lista, retorna um dicionário com o nome do time e os pontos na fase
assinatura: list --> dicionário'''
    j1=l[0]
    j2=l[1]
    t1=j1[0]#=j2[1]
    t2=j1[1]#=j2[0]
    r1=j1[2]
    r2=j2[2]
    s1j1=r1[0]
    s2j1=r1[1]
    s1j2=r2[1]
    s2j2=r2[0]
    if s1j1==s2j1:
        if s1j2==s2j2:
            p1=2
            p2=2
        if s1j2>s2j2:
            p1=4
            p2=1
        if s1j2<s2j2:
            p1=1
            p=4
    if s1j2==s2j2:
        if s1j1>s2j1:
            p1=4
            p2=1
        if s1j1<s2j1:
            p1=1
            p=4
    if s1j1>s2j1:
        if s1j2>s2j2:
            p1=6
            p2=0
        if s1j2<s2j2:
            p1=3
            p2=3
    if s1j1<s2j1:
        if s1j2>s2j2:
            p1=3
            p2=3
        if s1j2<s2j2:
            p1=0
            p2=6
    return {t1:p1,t2:p2}