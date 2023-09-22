def posLetra(texto,letra,num):
    total_letra=str.count(texto,str.lower(letra))+str.count(texto,str.upper(letra))
    if total_letra<numero:
        return -1
    indice = 0
    posicao = 0 
    qnt_de_vezes= total_letra-numero
    while str.count(texto,str.lower(letra),indice)+str.count(texto,str.upper(letra),indice)> qnt_de_vezes:
        if str.lower(letra) in texto[indice] or str.upper(letra) in texto[indice]:
            posicao = indice
        indice = indice + 1
    return posicao