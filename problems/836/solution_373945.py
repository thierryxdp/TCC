def busca(string,matriz):
    for linha in matriz:
        if string in linha:
            return linha
        else:
            return list()