def busca(setor,matriz):
    '''uma função que retorna todos os dados de todos funcionários do setor desejado de determinada empresa
    str, matriz -> matriz'''
    if str(setor) in not matriz:
        return []