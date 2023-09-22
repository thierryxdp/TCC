def eh_quadrada(matriz):
    'adkaajdj'
    c=0
    l=0

    for i in matriz:
        c+=1
        for j in matriz:
            l+=1

    if c==1 and l==1:
        return False
    
    if c == l:
        return True

    else:
        return False