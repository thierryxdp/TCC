def busca(setor, matriz):
    """dada uma matriz do tipo [[nome, registro, setor, telefone],...] e o setor, retorna todos os funcionários daquele
    setor
    :param setor: str
    :param matriz: lst(lst(str, str, str, str), ..., lst(str, str, str, str))
    :return: lst(lst, ..., lst)
    """
    listaRetorno = []
    for c in range(len(matriz)):
        if setor == matriz[c][2]:
            listaRetorno.append(matriz[c])
            
    return listaRetorno