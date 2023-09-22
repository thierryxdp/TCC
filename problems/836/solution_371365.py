def busca(buscandoPor,matriz):
    resultado=[]
    for nome,registro,setor,fone in matriz:
        if setor==buscandoPor:
            resultado.append([nome,registro,fone])
        return resultado