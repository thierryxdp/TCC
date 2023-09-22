def repetidos(ls):
    o=0
    fatia=ls[1:]
    for i in range(len(fatia)):
        if ft[i] == ls[i]:
            o=o+1
    return o