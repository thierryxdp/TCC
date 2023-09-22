def melhor_volta(x):
    for y in x:
    	p=min(y)
    	o=y.index(min(y))
    	if p in y:
            q=x.index(y)
    return (q,p,o)