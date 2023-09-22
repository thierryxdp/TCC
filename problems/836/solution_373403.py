def busca(s,mat):
    """Recebe um setor de uma empresa (string) e uma matriz
de dados dos funcionários no formato pré-estabelecido (strings).
Retorna uma lista que contém os dados dos funcionários que
tenham o setor inserido incluído em seus dados. Caso não haja
funcionários no setor inserido, retorma uma lista vazia.
str, mat -> list
"""
    selecionados = []
    for registros in mat:
        if registros[2]==s:
            dados = registros[:]
            list.remove(dados, registros[2])
            list.append(selecionados, dados)
    return selecionados