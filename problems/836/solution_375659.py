def busca(dic, setor):
	listinha=[]

    for linha in dic:
        for n in linha:
            if n==setor:
                listinha=dic[linha]
    return listinha