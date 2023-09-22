def busca(setor, matriz):
    resultado = list()

    
    for linha in matriz:
       
        if linha[2] == setor:
            resultado= resultado.append(list.pop([2]))
    return resultado