def pontos_por_time(lista1,lista2):
    lista1 = [time1,time2,[ida]]
    ida = [i1,i2]
    lista2 = [time2,time1,[volta]]
    volta = [v1,v2]
    resultado1 = ida1 + volta1
    resultado2 = ida2 + volta2
    if i1=i2:
        ida1=1
        ida2=1
    if i1>i2:
        ida1=3
        ida2=0
    if i1<i2:
        ida1=0
        ida2=3
    if v1=v2:
        volta1=1
        volta2=1
    if v1>v2:
        volta1=3
        volta2=0
    if v1<v2:
        volta1=0
        volta2=3
    resultado = {'time1':resultado1,
                 'time2':resultado2}
    return resultado