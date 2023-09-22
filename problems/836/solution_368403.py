def busca(dados,setor):
    '''Retorna os dados de todos os funionarios do setor.
    matriz,str->matriz'''
    lista=[]
    for i in tange(len(dados)):
        for j in range(len(dados[i])):
            if setor in dados[i]:
                lista+=dados[i]
                return lista
    return []