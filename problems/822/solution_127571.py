def repetidos(l1):
    i=0
    elem=0
    while i<len(l1):
        if l1[i]=l1[1-i]:
            elem=elem+1
        i=i+1
    return elem