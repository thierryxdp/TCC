def media_matriz(m):
    '''dado uma matriz calculamos a media dos elementos desta matriz'''
    '''list->flooat'''
    a=[]
    b=0
    for i in range (0,len(m)):
        for j in m[i]:
            a.append(j)
    for i in a:
        b+=i
    return round((b)/len(a),2)