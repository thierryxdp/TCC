def busca(listaContatos):
    contatinhos = []
    for i in range(len(listaContatos)):
        for j in range(len(listaContatos[0])): 
        	if str.lower(nome) in str.lower(listaContatos[i][j]):
            	contatinhos.append(listaContatos[i][j])
    return contatinhos