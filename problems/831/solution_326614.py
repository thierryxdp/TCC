def lingua_p(palavra):
    i=-1
    l=[]
    l2=[]
    c=list(palavra)
    i2=1
    i3=0
    d=''
    for x in palavra:
        i+=1
        if x in 'AÁÉEIOUÚaáeéioúu':
            b=str.find(palavra,x,i)
            list.append(l,b)
            list.append(l2,x)
    for x in l:
        list.insert(c,x+i2,'p'+l2[i3])
        i2+=1
        i3+=1
    for x in c:
        d+=x
    return d