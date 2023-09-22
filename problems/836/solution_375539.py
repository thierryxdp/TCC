def busca(setor,matriz):
    nova_lista = []
    for x in matriz:
        if setor in x:
            nova_lista.append(setor)
        return nova_lista
    	else: 
            return []