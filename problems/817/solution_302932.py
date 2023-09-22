#retorna lista com notas acima da média
#list-->list
def acima_da_media(j):
    l=sum(j)
    m=l/len(j)
    k=[]
    for x in j:
        if x>m:
            list.append(k,x)
    list.sort(k)
    return k