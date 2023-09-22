def posLetra(frase,letra,n):
    """Função que retorna a posição da string mediante a ocorrencia 'n' da letra 'l'
        str,str,int->int"""
    indice=0
    while indice < len(frase):
        if letra in frase:
            frase=str.replace(frase,letra,'/',n-1)
        indice=indice+1

    if letra in frase:
        return frase.index(letra)
    else:
        return -1