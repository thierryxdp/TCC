def busca(setor: str, dados_funcionarios: list)-> list:
    """Dado um nome de um setor da empresa e uma matriz contendo os dados dos
    funcionários, retorna os dados dos funcionários do setor dado."""

    setor_buscado = list()

    for funcionario in dados_funcionarios:
        if (setor in funcionario[2]):
            dados = funcionario[:]
            list.remove(dados, dados[2])
            list.append(setor_buscado,dados)

    return setor_buscado