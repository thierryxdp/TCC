def eh_quadrada(matriz):
    'adkaajdj'
    c=0
    l=0

    for i in range(len(matriz)):
        c+=1
        for j in range(len(matriz[i])):
            l+=1

    if c==1 and l==1:
        return False
    
    if c == l//c:
        return True

    else:
        return False