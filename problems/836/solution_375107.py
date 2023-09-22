def busca(setor, matriz):
    registro = []
    
    for lista in matriz:
    	if (setor in lista):
            lista.pop(setor)
            registro.append(lista)
    return registro