def media_matriz(mat): 
    soma = 0 
    contagem = 0
    for x in mat:
        for y in x:
            soma = soma + y
            contagem = contagem + 1
    media = round(soma/contagem,2)