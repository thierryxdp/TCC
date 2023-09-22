def busca(setor,m):
    """função que recebe uma matriz e um setor e faz uma busca na matriz dado o nome de um setor 
	str, list -> list"""
    
    busca_ = []
    for i in matriz:
        if i[2] == setor:
            list.append(busca_, i[:2] + i[3:])
    if busca_ != []:
        return busca_
    return []