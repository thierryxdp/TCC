def busca(setor,matriz):
    """Esta é a função que dada uma matriz e um nome de um setor da empresa, a função retorna os dados de todos os funcionários daquele setor, str, list -> list"""
    lista = []

    for l in range(len(matriz)):
        funcionario = matriz[l]
        s = funcionario[2]

        if setor in s:
            list.append(lista,funcionario)
                
    return lista