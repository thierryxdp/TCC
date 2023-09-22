def busca(string,matriz):
    busca=[]
    for linha in matriz:
        if string in linha:
            busca+=linha
            busca.remove(string)        
    return busca