def busca(d):
	d=[]
    for i in d:
        for j in i:
            if j==tipo:
                i.pop(2)
                d.append(i)
    return(d)