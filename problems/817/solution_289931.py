def acima_da_media(l):
    """Para listar as notas que ficaram a cima da média, digite;
    int->int"""
    a=sum(l)
    b=len(l)
    c=a/b
    
    if c not in l:
        list.append(l,c)
    	l=sorted(l)
    	x=list.index(l,c)
    	y=c+1
        return l[y:]