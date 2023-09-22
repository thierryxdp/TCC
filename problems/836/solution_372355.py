def busca(setor, m):
    """
    list(list) -> list"""
    lista = []
    for l in range(0,len(m)):
        if str.lower(m[l][2]) == str.lower(setor):
            dados = list.copy(m[l])
            list.pop(dados,m[l][2])
            list.append(lista,dados)
            
    return lista