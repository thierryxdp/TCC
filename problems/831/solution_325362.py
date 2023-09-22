def lingua_p(pl):
    '''traduz as palavras pra lingua do P. srt->str'''
    pl.lower()
    vogais = ['a','e','i','o','u','á','é','í','ó','ú']
    a=[]
    for x in pl:
        if a.count(x)==0:
            a.append(x)
    for vg in a:
        if vg in vogais:
            p= vg + 'p' + vg
            pl = str.replace(pl,vg,p)
    return pl