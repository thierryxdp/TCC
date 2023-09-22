def busca(setor,matriz):
    '''Recebe um setor de uma empresa e uma matriz dos funcionarios e retorna as informacoes
    dos funcionarios naquele setor
    str,matriz -> list'''
    lista=[]
    for linha in matriz:
        if linha[2]==setor:
            lista=[lista+[linha[0],linha[1],linha[3]]]
    return lista