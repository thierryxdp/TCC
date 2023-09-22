def busca(setor,matriz):
    func = []
    cont = 0
    for linha in matriz:
        for elemento in linha:
            if elemento == setor:
                func.append(linha)
		func[cont].remove(setor)
        cont += 1
    return func