def busca(setor,P):
    lista_retorno = []
    for i in P:
        if i[2] == setor:
            lista_retorno.append(i[0:2] + i[3:])
    return lista_retorno