def repetidos(x):
    elem=0
    i=0
    while i<len(x):
        if x[1]==x[2]:
            elem=elem+1
        i=i+1
    return elem