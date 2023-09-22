def busca(setor,lista):
    '''procura e retorna todos os funcionários e suas informações de um setor determinado
    	list,str->list'''
    
    res = []
    for i in range(len(lista)):
        if setor in lista[i]:
            res.append(lista[i][:])
    
    for i in range(len(res)):
        if setor in res[i]:
            res[i].remove(setor)
    return res