def repetidos(a):
    x=0
    z= a[0+x]==a[1+x]
    repeticao=0
    while x==len(a):
        if z== True:
            x= x+1
            repeticao+= 1
    return repeticao