def uppCons (frase):
    novafrase = ''
    tamanho = len(frase)
    indice = 0 
    while indice < tamanho:
        if frase[indice] not in 'aeiouAEIOU':
            novafrase += str.upper(frase[indice])
        else: 
            novafrase += frase[indice]
        indice += 1  
    return novafrase