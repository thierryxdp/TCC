def busca(funcionarios, setor):
    """Função que busca dentro de uma lista(contatos), os contatos que possuem
    um dado nome em parte de seu nome.
    lista, str --> lista"""
    resultadoBusca = []
    
    for funcionario in range(len(funcionarios)):
        if setor in str(funcionarios[2]):
            list.append(resultadoBusca,funcionarios[2])

    return resultadoBusca