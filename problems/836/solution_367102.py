def busca(setor, matriz):
    """Retorna os dados de todos os funcionarios do setor indicado;
       Entrada: str, list;
       Saida: list;
    """
    for i in setor:
        if setor in matriz:
            list.append(i[0], i[1], i[3])
    return list