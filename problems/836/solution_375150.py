def busca(setor, matriz):
    """
    	Recebe o nome do <setor> e a <matriz> com todos os
        dados dos funcionário.
        Retorna os dados dos funcionário que pertencem ao setor
        que foi buscado.
        str, list --> list
    """
    pesquisa = []
    for funcionario in matriz:
        if setor == funcionario[2]:
            copyDados = funcionario[:]
            list.remove(copyDados, setor)
            list.append(pesquisa, copyDados)
            
    return pesquisa