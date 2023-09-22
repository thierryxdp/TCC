def posLetra(frase,letra,ocorrencia):
    """A função retorna em que posição a string está, dada
	a ocorrência. str,str,int->int"""
    i=0
    batat=0
    while i<len(frase) and batat<ocorrencia:
        if frase[i] == letra:
            batat = batat +1
        i=i+1
    if batat<ocorrencia:
        return -1
    else:
        return i-1