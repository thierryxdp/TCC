def busca(setor,matriz):
    resultado = []
    for contato in matriz:
        if setor in contato:
            del contato[2]
            list.append(resultado,contato)
	return resultado