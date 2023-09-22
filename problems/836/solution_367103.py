def busca(setor, matriz):
    """Retorna os dados de todos os funcionarios do setor indicado;
       Entrada: str, list;
       Saida: list;
    """
    lista = []
    for i in matriz:
        for j in i:
            if setor in j:
            	list.append(lista, [i[0], i[1], i[3]])
    return lista