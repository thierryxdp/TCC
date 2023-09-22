def acima_da_media(l):
    media=sum(l)/len(l)
    k=[]
    for x in l:
        if x>media:
            k.append(x)
	k.sort()
    return k