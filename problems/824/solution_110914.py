def uppCons (frase):
    x=list(frase)
    k=0
    j=""
    while k<len(x):
        if x[k]not in ('a','ã','á','à','â','e','é','ê','i','í','o','ó','õ','ô','u','ú'):
            j=j+str.upper(x[k])
        else:
            j=j+x[k]
        k=k+1
	return j