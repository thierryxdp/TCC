def posLetra(frase,let,num):
    ''' str, str, int -> int'''
    x=int
    i=0
    y=2*num-1
    while i<len(frase):
        if num <= str.count(frase,let):
            x = str.find(frase,let,y)
        else:
            x=-1
        i+=1
    return x