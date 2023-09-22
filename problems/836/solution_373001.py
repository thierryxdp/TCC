def setor(reg):
    """Função que recebe o registro e retorna o setor
    em que o funcionário trabalha"""
    return reg[2]

def busca(s, mat):
    """Função que recebe uma matriz com as informações de 
    registro do funcionário e o setor que você deseja buscar
    nesse registro.
    mat,str->list"""
    retorno = []
    for r in mat:
        if setor(r) == s:
                ls = list.copy(r)
                del ls[2]
                list.append(retorno, ls)
    return retorno