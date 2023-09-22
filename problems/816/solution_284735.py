def maiores(numeros: list[int],n: int) -> list[int]:
     # Obtendo uma copia da lista numeros
    numerosCopia = numeros.copy()

##    # Adicionando o numero n na lista
    numerosCopia.append(n)
##
##    # Ordenando a lista para colocar n na sua respectiva
##    # posicao
    numerosCopia.sort()
    
    # Indentificar o indice onde foi colocado o numero n
    posicaoN = numerosCopia.index(n)

    # Obtendo os numeros maiores que n usando fatiamento
    numerosMaiores = numerosCopia[posicaoN+1:]
    
    if n in numerosMaiores.count(n):
    	numerosMaiores = numerosMaiores[quantidade:]
  
  
    return numerosMaiores