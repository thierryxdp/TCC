def acima_da_media(x):
    m = sum(x)/len(x)
    list.sort(x)
    list.insert(x,(int(m)+1), m)        
    return x[(list.index(x,m)+1+(x.count(m)-1))::]