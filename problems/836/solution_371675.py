def busca(setor,matriz):
    '''Recebe um setor de uma empresa e uma matriz com as informacoes dos funcionarios, e retorna
    uma lista com as informacoes dos funcionarios do setor
    str,matrizz -> list'''
    lista=[]
    for linha in matriz:
        if linha[2]==setor:
            lista=lista+[linha[0],linha[1],linha[3]]
    return [lista]