def posLetra(string,letra,n):
    n=0
    while str.find(string,letra)<str.index(string,letra,n):
        if str.find(string,letra)<str.index(string,letra,n):
            return str.index(string,letra,n)
        elif str.index(string,letra,n)== str.find(string,letra):
            return -1
        elif n<str.find(string,letra):
            return str.find(string,letra)
        
    else:
        return -1