def busca(setor, funcionarios):
    matriz = []
    for funcionario in funcionarios:
        if setor == funcionario[1]:
            f = funcionario[:1]+funcionario[2:]
            matriz.append(f)
    return matriz