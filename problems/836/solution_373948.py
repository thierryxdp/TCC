def busca(string,matriz):
    busca=[]
    for linha in matriz:
        if string in linha:
            busca.append(linha)
    return busca