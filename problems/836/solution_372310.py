def busca(setor:str,m:list)->list:
    lista=[] #lista para busca
    for i in range(len(m)):
            if setor==(m[i][2]):#teste de setor
                m[i].pop(2)# retirada do setor
                lista.append(m[i])# adição de dados a lista
                
                
                
                
             
	return lista