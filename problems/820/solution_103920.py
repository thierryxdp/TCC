def posLetra (frase,letra,n):
    ocorrencia=[]
    tamanho=0
    if str.count(frase,letra)<n:
        return -1
    while tamanho>n:
        if letra == frase[tamanho]:
            ocorrencia=ocorrencia+[tamanho,]
        tamanho=tamanho+1
    return ocorrencia[-1]