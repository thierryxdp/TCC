def busca(setor, matriz):
    res=[]
    
    for linha in matriz:
       
        if linha[2] == setor:
            linha.pop(2)
            res.append(linha)
    return linha