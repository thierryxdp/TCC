def busca(setor,m):
    """Função que recebe uma matriz e uma string e retorna todas as linhas que contem 
    a string
    list,string --> list"""
    r = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == setor:
                p = [m[i][0],m[i][1],m[i][3]]
                list.append(r,p)
	return r