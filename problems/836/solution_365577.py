def busca(setor,matriz):
    """dado o setor e a matriz
verifica os contatos dentro da empresa
que correspondem com o setor"""
    contatos = []
    for i in matriz[i]:
        if setor == matriz[i][2]:
            contatos += matriz[i][2]

    return contatos