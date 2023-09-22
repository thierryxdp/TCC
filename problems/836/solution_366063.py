def busca(setor,matriz):
    
    linhas = len(matriz)
    nova_m = []
    m_final = []
    
    for linha in range(linhas):
        colunas = len(matriz[0])
        
        for coluna in range(colunas):
            
            if matriz[linha][coluna] == setor:
                
                nome = matriz[linha][0]
                codigo = matriz[linha][1]
                telefone = matriz[linha][3]
                
                list.append(nova_m, nome)
                list.append(nova_m, codigo)
                list.append(nova_m, telefone)
                list.append(m_final, nova_m[:])
                
		list.clear(nova_m)
        
	return m_final