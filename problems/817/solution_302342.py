def acima_da_media(a):
    t1=[i for i in a if i>sum(a)/len(a)]
    return sorted(t1)