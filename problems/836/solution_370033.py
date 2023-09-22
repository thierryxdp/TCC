def busca(setor,matriz):
    result=[]
    for funcionario in matriz:
        if setor in funcionario:
            result.append(funcionario.remove(setor))
    return result