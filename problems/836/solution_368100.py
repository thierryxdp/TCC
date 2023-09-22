def busca(setor, matriz):
    resultado = list()

    
    for linha in matriz:
       
        if linha[2] == setor:
            linha.pop(2)
            resultado= resultado.append(linha)
                                      
    return resultado