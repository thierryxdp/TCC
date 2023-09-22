# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    '''A função recebe como entrada duas listas, e retorna uma única lista,
       composta pelos elementos das listas originais; de forma que estarão organizados 
       de forma intercalada. Ex: [lista1[0],lista2[0],lista1[1],lista2[1],...]'''

	L1 = lista1
	L2 = lista2
    L3 = []
    i = 0
    while i < max(len(L1),len(L2)):
		if len(L1) > i:
        	L3.append(L1[i])
		if len(L2) > i:
        	L3.append(L2[i])       
        i+=1
    return L3