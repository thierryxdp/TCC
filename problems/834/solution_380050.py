def media_matriz(m):
    
    tamanho=len(m)*len(m[0])
    soma=0
    
    for linha in matriz:
        for posicao in linha:
            soma+=posicao
            
    return soma/tamanho