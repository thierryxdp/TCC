def busca(setor,matriz):
    result=[]
    for funcionario in matriz:
        if setor in funcionario:
            result.append(funcionario[2:5:1])
    return result