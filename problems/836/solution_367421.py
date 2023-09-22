def busca(setor,matriz):
    funcionarios_encontratos = []
    for dados in matriz:
        for funcionarios in dados:
            if setor in funcionarios:
                funcionarios_encontratos.append(dados)
    return funcionarios_encontratos