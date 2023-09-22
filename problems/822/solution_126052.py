def repetidos(lista):
  
    
    indice = 0
    contagem = 0
    
    while indice<len(lista)-1:
        if(lista[indice] == lista[indice+1]):
            contagem = contagem+1
        indice = indice+1
    return contagem