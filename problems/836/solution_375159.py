def busca(setor, matriz):
    lista_retorno = []
    fori in matriz:
        if i[2] == setor:
            lista_retorno.append(i[0:2] + i[3:])
    return lista_retorno