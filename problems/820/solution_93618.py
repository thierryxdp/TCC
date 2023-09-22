def posLetra(texto,letra,numero):
    """Funçao que dada duas str e um numero caclcula se na str texpo possui a str letra e o numero de vezes que aparece dando a posiçao se possuir o numero de vezes que aparece se nao retorna -1
    str, str, int -> int"""
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