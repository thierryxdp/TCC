def intercala(L1,L2):
    '''funçao que dadas duas listas L1 e L2 de tamanho 3, gera uma lista L3 que e formada 
intercalando os elementos de L1 e L2 
int,list-->list'''
	L3 = [L1[0],] + [L2[0],] + [L1[1],] + [L2[1],] + [L1[2],] + [L2[2],]
return L3