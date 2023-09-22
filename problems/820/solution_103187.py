def posLetra(string,letra,n):
    
    i= str.find(string,letra)
    while i>=0 and n>1:
        i= str.find(string,letra,i+1)
        n-=1
        return i