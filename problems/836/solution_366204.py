def busca(setor, matriz):
    """Retorna todos os dados de todos osfuncionários de tal setor; string, list -> list."""
    lista2 = []
    for i in range(0,len(matriz)):
        z = matriz[i][:]
        if setor in z[2]:
            list.append(lista2, matriz[i])
    return lista2