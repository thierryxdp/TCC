def busca(dic, setor):
	listinha=[]
	
    for linha in dic:
        if linha[2]==setor:
            listinha.append(linha[:2:]+linha[3:])
    return listinha