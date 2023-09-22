def filtraMultiplos(lista, x):
  # '''
	#Essa função irá filtrar os numeros dados na lsita = lista e irá retornar outra 
    #outra lista todos os números que forem divididos pelo número oferecido na variável n.
    #Entrada: lista | Saída: Lista
   #'''
	multi = []
    for i in range(len(lista)):
        if lista[i]%x == 0:
            multi.append(lista[i])
    return multi