def PosiçãoLetra(frase,letra,numero):'
    if frase.count(letra)<numero:
        return -1
    t=0
    h=0
    while h!=numero:
        if letra==frase[t]:
            posicao=t
            h=h+1
        h=h+1
    	return posicao