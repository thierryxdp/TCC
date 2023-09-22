def busca(setor,matriz):
    funcionarios_encontratos = []
    for dados in matriz:
        for funcionarios in dados:
            if setor in funcionarios:
                dados.remove(setor)
                funcionarios_encontratos.append(dados)
    return funcionarios_encontratos