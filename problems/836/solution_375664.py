def busca(dic, setor):
	listinha=[]

    for linha in dic:
        for n in linha:
            i=dic.index(linha)
            if dic[i][2]==setor:
                listinha=dic[linha]
    return listinha