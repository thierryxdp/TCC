def busca(setor,m):
    """Função que recebe uma matriz e retorna os dados de todos os
    funcionários daquele setor; list, str-> list"""
    soma=0
    lista1=[]
    for empregado in m:
        if setor in empregado[2]:
            list.append(empregado,lista1)
            list.remove(setor,lista1[soma])
            soma+=1
    return lista1