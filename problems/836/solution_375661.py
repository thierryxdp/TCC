def busca(dic, setor):
	listinha=[]

    for linha in dic:
        for n in linha:
            list.index(linha,n)
            if dic[linha][n]==setor:
                listinha=dic[linha]
    return listinha