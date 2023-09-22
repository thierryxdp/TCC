def acima_da_media(ls):
    if ls[0]==ls[0]/len(ls):
        return []
    r=0
    for x in ls:
        if x>0:
            r+=x
    med=r/len(ls)
    ls.append(med)
    ls.sort()
    return ls[ls.index(med)+1:]