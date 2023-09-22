def busca(setor,matriz):
    """dado o setor e a matriz
verifica os contatos dentro da empresa
que correspondem com o setor"""
    contatos = []
    LinhaMatriz = len(matriz)
    
    for i in range(LinhaMatriz):
        
        ColunaMatriz = matriz[i][2]
        if setor == ColunaMatriz:
            
            contatos += [[matriz[i][0],matriz[i][1],matriz[i][3]]
                          

    return contatos