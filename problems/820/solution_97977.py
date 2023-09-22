def posLetra(frase,letra,ocorrencia):
    lista = list (frase)
    cont = lista.count(letra)
    
    if cont >= ocorrencia:
    	substitui = str.replace(frase,letra,'&',ocorrencia - 1)
    	return str.find(substitui,letra,0,-1)
    else:
        return -1