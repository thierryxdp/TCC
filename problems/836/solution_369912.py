# QUESTÃO 5 - OK!
def busca(m,s):
    """ Dado uma matriz (nome,registro,setor,telefone) e um setor vamos retormar o(s) funcionario(s) que trabalham nesse setor.
        Parametros:
        Entrada -> matriz : list
        Saida   -> list   """
    lista=[]
    num_linha=len(m)
    num_coluna=len(m[0])

    for i in range(num_linha):
        if s in m[i][2]:
            mome=m[i][0]
            registro=m[i][1]
            tel=m[i][2]
            list.append(lista,nome)
            list.append(lista,registro)
            list.append(lista,tel)
    return lista