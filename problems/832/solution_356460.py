def eh_quadrada(matriz):
    'adkaajdj'
    c=0
    l=0

    for i in range(len(matriz)):
        c+=1
        for j in range(len(matriz[i])):
            l+=1

    if c==0 and l==0:
        return True
    
    if c == l//c:
        return True

    else:
        return False