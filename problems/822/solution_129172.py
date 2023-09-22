def repetidos(ls):
    o=0
    ft=ls[1:]
    for i in range(len(ft)):
        if ft[i]==ls[i]:
            o+=1
    return o