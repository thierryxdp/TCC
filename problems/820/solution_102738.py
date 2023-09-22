def posLetra(palavra,letra,n):
    if n==1:
        return str.find(palavra,letra,n)
        
    else:
        return str.find(palavra,letra,n+2,n+4)