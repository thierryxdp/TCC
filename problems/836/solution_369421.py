def busca(matriz,setor):
	'''função que dada uma matriz (onde cada linha contém informações 
    referentes a uma pessoa e cada coluna represente respectivamente
    o nome, o registro, o setor e o telefone de cada pessoa, todos os 
    dados em formato de string), e um setor, retorne os dados de todas
    as pessoas daquele setor;
    list,str-->list'''
    
	contatos=len(matriz)
	encontrados=[] #contatos encontrados
    
	for buscar in range(contatos):
		if setor in matriz[buscar]:
			list.append(encontrados,matriz[buscar])
            
	return encontrados