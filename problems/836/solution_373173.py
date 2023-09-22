def busca(setor,m):
    """funcao que, dado um setor da empresa, retorna dados de todos os funcionarios desse setor. list,str->list"""
    lista=[]
    for i in range(len(m)):
        if m[i][2] == setor:
            list.remove(m[i],m[i][2])
            lista.append(m[i])
            return lista