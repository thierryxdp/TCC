def posLetra(string,letra,num):
    i=0
    num=[]
    while i<=len(string)-1:
        if string[i]==letra:
            num.append(i)
        i=i+1
    return num[(num-1)]