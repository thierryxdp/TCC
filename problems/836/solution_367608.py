def busca(informacao, matriz):
    """A funcao busca tem como finalidade apresentar quais sao os funcionarios de uma
    empresas que estao em determinado setor. Para isto, a funcao recebe como entrada uma
    informacao e uma matriz contendo a ficha completa dos funcionarios; e retorna esta ficha,
    mas sem o nome do setor.
    Entrada: int, list
    Retorno: list"""
    setor = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if str.count(informacao,matriz[i][j])>0:
                setor += (matriz[i][0:j] + [matriz[i][j + 1]],)
    return setor