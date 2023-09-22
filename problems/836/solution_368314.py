def busca(setor,matriz):
    """
    srt,lista->lista ou str
    :param setor: Recebe uma lista e busca dentro desta, o setor, função e numero
    :param matriz: Recebe uma matriz com os dados de uma empresa 
    :param return: Retorna os registros de um setor
    """
    funcionarios = (len(matriz))
    dados = (len(matriz[0]))
    lista_setor = []
    for busca in range(funcionarios):
        lista_busca = []
        for dados in range(dados):
            if matriz[busca][dados] == setor:
                list.append(lista_busca,matriz[busca][0])
                list.append(lista_busca,matriz[busca][1])
                list.append(lista_busca,matriz[busca][3])
        if len(lista_busca)>=1:
            list.append(lista_setor,lista_busca)
    if len(lista_setor) == 0:
        return []
    return lista_setor