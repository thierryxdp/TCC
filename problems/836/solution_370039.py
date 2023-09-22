def busca(setor,matriz):
    result=[]
    for funcionario in matriz:
        if setor in funcionario:
            result.append(funcionario[3:3:1])
    return result