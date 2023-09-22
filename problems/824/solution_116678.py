def uppCons (frase):
    i=0
    f=list(frase)
    f1=[]
    while i<len(frase):
        if f[i]in 'bcdfghjklmnpqrstvxwyz':
            f2=str.upper(frase[i])
            list.append(f1,f2)
        else:
            list.append(f1,f[i])
        i=i+1
    f3 = str(f1)
    f4=f3.replace("'","")
    f5=f4.replace(",","")
    f6=str(f5).strip('[]')
    return f6