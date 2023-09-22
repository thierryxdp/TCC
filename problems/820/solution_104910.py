def posLetra(frase, letra, ocorrencia):
	letras = str.split(frase, '')
    indexs = []
    for n in letras:
        if n == letra:
            indexs.append(n.index())
    
    if len(indexs) <= ocorrencia:
        return indexs[-1]
    else:
        return -1