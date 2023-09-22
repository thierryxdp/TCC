def busca(cargo,m):
    """ Funcao que recebe uma string "cargo" e uma matriz "m"
    de entrada e retorna a busca do funcionario de acordo com
    o setor em que ele trabalha, retornando seus dados em uma lista """
    """ str, list -> list """
    busca=[]
    for L in range(0,len(m)):
        for C in range(0,len(m[L])):
            if cargo == m[L][C]:
                pesquisa = list.copy(m[L])
                pesquisa.pop(pesquisa.index(pesquisa[C]))
                list.append(busca,pesquisa)
    return busca
#casos de teste:
""" m=[["adal", "566", "contab", "21999"],["ju","465","RH","21888"],["fla","565","contab","211010"]]
>>> [['adal', '566', '21999'], ['fla', '565', '211010']] """