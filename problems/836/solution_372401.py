def busca(setor,dados):
    """faz uma busca por setor e retorna todos os dados
    de todos os funcionarios do mesmo dado.
    str,list(of lists)->list"""
    resultado=[]
    for pessoa in dados:
        if setor in pessoa:
            pessoa.remove(setor)
            resultado.append(pessoa)
    return resultado