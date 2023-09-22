def posLetra(texto,l,n):
    texto = list(texto)
    cont = texto.count(l)
    
    if cont>=n:
        substitui = str.replace(texto,l,'&',n-1)
        return str.find(substitui,l,0,-1):
    else:
        return -1