def busca(funcionarios, setor):
    """Função que busca dentro de uma lista(contatos), os contatos que possuem
    um dado nome em parte de seu nome.
    lista, str --> lista"""
    resultadoBusca = []
    
    for funcionario in range(len(funcionarios)):
        if str(setor) in str(funcionarios[funcionario][1]):
            list.append(resultadoBusca,funcionarios[funcionario])

    return resultadoBusca