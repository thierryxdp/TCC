def acima_da_media(x):
    m = sum(x)/len(x)
    x.append(m)
    list.sort(x)        
    return x[(list.index(x,m)+x.count(m))::]