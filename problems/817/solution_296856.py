def acima_da_media(notas):
    x=sum(notas)/len(notas)
    green=list()
    for h in notas:
        green.append(h)
        if h>x:
            list.sort(green)
    return green