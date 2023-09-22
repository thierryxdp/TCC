def posLetra(string,letra,n):
    h=string.find(letra)
    while h >=0 and n>1:
        h=string.find(let,h+ 1)
        n=n- 1
    return h