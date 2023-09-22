def busca(setor,m):
    """Função que recebe uma matriz e"""
    soma=0
    lista1=[]
    for empregado in m:
        if setor in empregado[2]:
            list.append(empregado,lista1)
            list.delete(lista1[soma][2],lista1)
    return lista1