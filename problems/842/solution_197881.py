def pontos_por_time(a):
    somatime1 = 0
    somatime2 = 0
    if a[0][2][0] >a[0][2][1]:
        somatime1 = somatime1 + 3
    if a[0][2][0] == a[0][2][1]:
        somatime1 = somatime1 + 1
        somatime2 = somatime2 + 1
    if a[0][2][0]<a[0][2][1]:
        somatime2 = somatime2 + 3
    if a[1][2][0] >a[1][2][1]:
        somatime2= somatime2+ 3
    if a[1][2][0] == a[1][2][1]:
        somatime1 = somatime1 + 1
        somatime2 = somatime2 + 1
    if a[1][2][0] < a[1][2][1]:
        somatime1= somatime1+ 3
    if somatime1 > somatime2:
        return a[0][0]+':'+ str(somatime1), a[0][1]+':'+ str(somatime2)
    if somatime1 < somatime2:
        return a[0][1]+':'+ str(somatime2), a[0][0]+':'+ str(somatime1)
    if somatime1 == somatime2 and a[1][2][0] >a[1][2][1]:
        return a[0][1]+':'+ str(somatime2), a[0][0]+':'+ str(somatime1)
    if somatime1 == somatime2 and a[1][2][0] < a[1][2][1]:
        return a[0][0]+':'+ str(somatime1), a[0][1]+':'+ str(somatime2)