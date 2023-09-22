def lingua_p(palavra):
    
    listaP = str.split(palavra)
    iLista = 0
    
    for letra in listaP:
        if letra in 'AEIOUaeiou':
            indice = listaP.index(letra)
            listaP.insert(indice+1, 'p' + letra)
        
        else:
            pass
  
	return listaP