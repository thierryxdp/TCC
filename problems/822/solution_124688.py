def repetidos(lista):
    cont1 = 1
    x = []
    x.append(lista[0])
    while (cont1 < len(lista)):
        
        existe = 0
        cont2 = 0
        while (cont2 < len(x)):
        	if x[cont2] == lista[cont1]:
            	existe = 1
            cont2 = cont2 + 1
        if not existe:
            x.append(lista[cont1])
        
        cont1 = cont1 + 1
        
    return len(x)