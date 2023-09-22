def busca(pesquisa, matriz):
    """Função que receba uma matriz e irá fazer uma busca dado o nome ou o setor da empresa buscado
e deve me retornar os dados de todos os funcionarios que são presentes naquele setor. str, matriz -> lista"""
    
    setor = []
    pesquisa = ''
    for cargos in range (len(matriz)):
        if pesquisa in matriz[cargo]:
            setor += [matriz[cargos][0],matriz[cargos][1],matriz[cargos][3]]
        else:
            setor = []
    return setor