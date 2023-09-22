def repetidos(l):
    i=1
    cont=0
    while i<len(l):
        if l[i]==l[i-1]:
            cont+=1
        i+=1
    return cont