def busca(setor,matriz):
    resultado=[]
    for linha in matriz:
        if setor in linha:
            linha=resultado
            del resultado[2]
    return resultado