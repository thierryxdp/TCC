def busca(setor, funcionarios):
    matriz = []
    for funcionario in funcionarios:
        if setor == funcionario[2]:
            f = funcionario[:2] + funcionario[3:]
            list.append(matriz, f)
    return matriz