def busca(setor,matriz):
    result=[]
    for funcionario in matriz:
        if setor in funcionario:
            fun=funcionario
            fun.remove(funcionario[2])
            result.append(fun)
    return result