def busca(setor, matriz):
    registro = []
    
    for lista in matriz:
    	if (setor in lista):
            registro.append(lista)
    return registro