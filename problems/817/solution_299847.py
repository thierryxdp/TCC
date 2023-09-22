def acima_da_media(a):
	soma=0
    for i in range(len(a)):
		soma=soma+a[i]
	d=len(a)
    me=soma/d
    f=[]
    for j in range(len(a)):
        if(a[j]>me):
            f.append(a[j])
    return sorted(f)