def lingua_p(p):
    lista=[]
    for i in range(0,len(p)):
        if palavra[i] in 'AEIOUaeiou':
           	p.split(p[i])
           	i=i+1
   	return p[i] + 'pe' + p.split(p[i])[0]+p[i]+'pe'+p.split(p[i])[1]+p[i]+'pe'+p.split(p[i])[2]+'plo'