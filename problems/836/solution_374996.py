def busca(setor,matriz):
    resultado=[]
    for linha in matriz:
        if setor in linha:
            resultado=linha
            del resultado[2]
    return resultado