def media_matriz (m):
    ''' '''
    ''' '''
    final = []
    for numero in m:
        for i in numero:
            final+=[i,]
     
    media = round(sum(final)/len(final),2)
    return media