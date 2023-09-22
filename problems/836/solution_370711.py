def busca(setor,funcionarios):
    """Função que busca dentro de uma lista(contatos), os contatos que possuem
    um dado nome em parte de seu nome.
    lista, str --> lista"""
    resultadoBusca = []
    
    for funcionario in range(len(funcionarios)):
        if setor in funcionarios[funcionario][2]:
            list.append(resultadoBusca,list.pop(funcionarios[funcionario][2]))

    return resultadoBusca