def busca(setor,matriz):
    result=[]
    for funcionario in matriz:
        if setor in funcionario:
            result.append(funcionario[4:2:-1])
    return result