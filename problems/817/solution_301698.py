def acima_da_media(x):
    s= [n for n in x if n>(sum(x)/(len(x)]
    list.sort(s)
    return s