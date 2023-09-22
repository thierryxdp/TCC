def retira_pontuacao(pal):
    d={'.':'',':':'',';':'','-':'',',':'','?':'','!':''}
    for x in d:
        pal=str.replace(pal,x,d[x])
        return pal
    
    
def inverte(pal):
    pal=retira_pontuacao(pal)
    pal=str.lower(pal)
    pal=str.split(pal)
    pal=pal[::-1]
    pal=str.join('',pal)
    return pal