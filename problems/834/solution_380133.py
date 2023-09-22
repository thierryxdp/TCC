def media_matriz(media):
    
    m = 0
    a = len(media)
    b = len(media[0])
    total = (a)*(b)
    
    for i in range (a):
        for j in range(b):
            m = m + media[i][j]
    final = m / total
            
    return %02.2f %final