def inverte(i) :
    i=i.replace("!"," ").replace("-"," ").replace("?"," ").replace("..."," ").replace("."," ").replace(","," ").lower()
    j=i.split()
    k=j[::-1]
    l=str.join(" ",k)
    return l