def busca (setor,matriz):
    '''retorna os dados de todos os funcionários
    do setor. 
    string, lista-> lista'''
    inf = []
   
    
    for linhas in range(len(matriz)): 
        if setor in matriz[linhas]:
            inf.append(matriz[linhas])
            
    for j in range(len(inf)):
        if setor == inf[j][2]:
            del inf[j][2]
            
                
   	return inf