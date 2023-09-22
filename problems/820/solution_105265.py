def posLetra(texto,letra,ocorr):
	if 0<ocorr<=texto.count(letra):
        i=0
        while ocorr>0:
            i=texto.index(letra,i)
            ocorr-=1
        return i
    return -1