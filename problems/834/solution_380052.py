def media_matriz(m):
    
    tamanho=len(m)*len(m[0])
    soma=0
    
    for linha in m:
        for posicao in linha:
            soma+=posicao
            
    return round(soma/tamanho,2)