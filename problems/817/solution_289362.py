def acima_da_media(x):
    """A funçao calcula a media das notas da lista dada como parametro,
     e gera uma nova lista com as notas acima da média.list-->list"""
    y = int(sum(x)/len(x))
    list.append(x,y)
    list.sort(x)
    s = list.index(x,y)
    return x[s+1:]