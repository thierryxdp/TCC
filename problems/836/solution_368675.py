def busca(setor,matriz):
    """funcao que retorna os funcionarios que trabalham em um
    determinado setor;str,list->list"""
    funcionarios=[]
    for i in range(len(matriz)):
    	if matriz[i][2]==setor:
            funcionarios=funcionarios+[matriz[i][0]+matriz[i][1]+matriz[i][3]]
    return funcionarios