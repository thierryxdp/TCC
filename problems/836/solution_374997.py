def busca(setor,matriz):
    resultado=[]
    ale=[]
    for linha in matriz:
        if setor in linha:
            resultado=linha
            del resultado[2]
            list.append(ale,resultado)
    return resultado