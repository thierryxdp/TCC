def busca(setor, matriz):
    resultado = list()

    
    for linha in matriz:
       
        if linha[2] == setor:
            
            resultado.append(linha)

   
    return resultado