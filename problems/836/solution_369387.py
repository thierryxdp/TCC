def busca(setor,m):
    """Função que recebe uma matriz e retorna os dados de todos os
    funcionários daquele setor; list, str-> list"""
    lista1=[]
    for empregado in m:
        if setor in empregado[2]:
            list.append(lista1,empregado[:2]+[empregado[3]])
    return lista1