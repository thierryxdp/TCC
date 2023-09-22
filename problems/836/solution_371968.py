def busca(setor,matriz):
    '''dados uma matriz e um setor da empresa, retorna os 
    dados de todos od funcionarios daquele setor
    list,'''
    
    a=[]
    
    for i in range(len(matriz)):
        	if setor in matriz [i]:
           		matriz[i].remove(setor)
               	a=a+[matriz[i]]
    return a