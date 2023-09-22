def busca(setor, matriz):
    resultado = list()

    
    for linha in matriz:
       
        if linha[2] == setor:
            
            resultado.append(linha[0,1,3])

   
    return resultado