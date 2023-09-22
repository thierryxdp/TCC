def posLetra(frase,letra,x):
    j=list(frase)
    posx=-1
    let=0
    if letra in frase and list.count(j,letra)>=x:
        while let<x:
            posx=posx+1
            if j[posx]==letra:
                let=let+1                
        return posx
    else:
        return -1