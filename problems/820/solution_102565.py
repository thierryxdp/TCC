def posLetra(frase,let,num):
    ''' str, str, int -> int'''
    x=int
    i=0
    y=num-1
    while i<len(frase):
        if num <= str.count(frase,let):
            z=str.replace(frase,let,'*',y)
            x = str.find(z,let,0)
        else:
            x=-1
        i+=1
    return x