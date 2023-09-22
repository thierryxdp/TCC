def media_matriz(matriz):
    ''''''
    soma=0
    quant=0
    
    for linha in matriz:
        soma=soma+sum(linha)
        quant=quant+len(linha)
        
    return round(soma/quant,2)