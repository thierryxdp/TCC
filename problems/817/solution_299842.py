def acima_da_media(a):
	for i in range(len(a)):
        for j in range(i,len(a)):
            if(a[j]<a[j+1]):
                d=a[j]
                a[j+1]=a[j]
                a[j]=d
                
	return a