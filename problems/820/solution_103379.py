def posLetra(frase,letra,numero):
    i=0
    ocorre=''
    local=0
    while i<len(frase):
        if frase[i] in letra:
            ocorre=ocorre+frase[i]
            if len(ocorre)<numero:
                return -1
            else:
                frasey=str.replace(frase,letra,'&',numero-1)
                
        i=i+1
    return str.find(frasey,letra)