def busca(dados,setor):
    '''Retorna os dados de todos os funionarios do setor.
    matriz,str->matriz'''
    lista=[]
    for i in range(len(dados)):
        for j in range(len(dados[i])):
            if setor == dados[i]:
                lista+=dados[i]
                return lista
    return []