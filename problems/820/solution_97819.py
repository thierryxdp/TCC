def posLetra(frase,letra,x):
    j=list(frase)
    posx="posição da x aparição da letra"
    k=0
    l=0
    if letra in frase and list.count(j,letra)>=x:
        while k>x:
            if j[l]==letra:
                posx=posx+1
			k=k+1                
        return posx
    else:
        return -1