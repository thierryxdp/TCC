def busca(matriz:list, setor:str)->list:
    """Dada uma matriz com as informações de cada funcionário por linha e 
       com colunas sendo respectivamente nome, registro, setor e telefone
       a função filtra a matriz no setor inserido
       
       Parameters:
       matriz: matriz com 4 colunas(nome, registro, setor e telefone) e
       linhas são por funcionário então pode variar
       
       Returns:
       lista com informaçãoes dos funcionário de determinado setor
    """
    nlin = len(matriz)
    
    filtrados = []
    
    for funcionario in range(nlin):
    	if setor in matriz[funcionario][2]:
        	list.append(filtrados,[matriz[funcionario][0:2]+matriz[funcionario][-1]])
    return filtrados