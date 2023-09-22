def busca(setor_busca):
    """retorna os dados do setor"""
    if setor == matriz[1][3]:
        return [nome[1][0:], registro[1][1:], telefone[1][3:]]
    else:
        return [[nome[0][0:], registro[0][1:], telefone[0][3:]], [nome[2][0:], registro[2][1:], telefone[2:][3:]]]