def filtraMultiplos(lista, x) :
    #Essa função irá filtrar os números de uma lista da variável lista e retornar ouutra lista 
    #com os elementos que forem divisíveis pelo número da variável n
	#entrada: lista | saída: lista
    multi = []
    i = 0
    while i < len(lista):
        if lista[i]%x == 0 :
            multi.append(lista[i])
        i += 1
        
    return multi