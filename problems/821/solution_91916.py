def posLetra(texto,letra,ocorr):
    """Retorna em que posição de uma string(texto) a ocorrencia fornecida(ocorr) de uma letra(letra) está.
    str,str,int->int"""
	if 0<ocorr<=texto.count(letra):
        i=0
        while ocorr>0:
            i=texto.index(letra,i)
            ocorr-=1
        return i
    return -1