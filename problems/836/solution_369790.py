def busca(setor: str , lista: list) -> list:
    """Dado o nome de um setor da empresa e a lista de funcionários, 
    a função retorna uma lista com os dados de todos os funcionários daquele setor"""
    
    lista2 = []
    for i in range(len(lista)):
        if setor in lista[i][2]:
            del lista[i][2]
            list.append(lista2, lista[i])
    return lista2