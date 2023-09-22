def busca(setor,matriz):
    '''Recebe um setor de uma empresa e as informacoes dos funcionarios e retorna uma lista com
    as informacoes dos funcinarios do setor
    str,matriz -> list'''
    lista=[]
    for linha in matriz:
        if setor in linha:
            linha.remove(setor)
            lista=lista+[linha]
    return lista