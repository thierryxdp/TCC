def busca(setor,matriz):
    resultado = []
    for funcionario in matriz:
        if setor in funcionario:
            list.append(resultado,[funcionario[0],funcionario[1],funcionario[3]])
    return resultado