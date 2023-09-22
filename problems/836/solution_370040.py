def busca(setor,matriz):
    result=[]
    for funcionario in matriz:
        if setor in funcionario:
            result.append(funcionario[3:2:1])
    return result