def busca(string,matriz):
    busca=[]
    for linha in matriz:
        if string in linha:
            remover=linha.remove(string)
            remover.append(linha)
    return busca