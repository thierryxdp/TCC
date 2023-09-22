def setor(reg):
    return reg[2]

def busca(s, mat):
    '''Analisar mat e retornar as pessoas
    que trabalhem no /setor/ pedido pelo usuário.'''
    ret = []
    for r in mat:
        if setor(r) == s:
            ls = list.copy(r)
            del ls[2]
            list.append(ret, ls)
    return ret