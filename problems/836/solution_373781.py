def setor(reg):
    return reg[2]
def busca(s, mat):
    """ dado o nome de um setor, retorna os dados dos funcionarios desse setor."""
    ret = []
    for r in mat:
        if setor(r) == s:
            ls = [r[0], r[1], r[3]]
            list.append(ret,ls)
    return ret