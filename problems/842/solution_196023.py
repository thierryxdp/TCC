def pontos_por_time(i):
    cormengo=()
    flaminthians=()
    p=i[0]
    s=i[1]
    p1=p[2]
    s1=s[2]
    if p1[0]>p1[1]:
             cormengo=cormengo+3
    if p1[0]==p1[1]:
             cormengo=cormengo+1
    if s1[0]>s1[1]:
             flaminthians=flaminthians+3
    if s1[0]==s1[1]:
             flaminthians=flaminthians+1
    return {(p[0]):cormengo,(p[1]):flaminthians} or {(p[1]):cormengo,(p[2]):flaminthians}