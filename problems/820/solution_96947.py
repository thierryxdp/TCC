def posLetra(texto,letra,n):
    """Função que retorna a posição da string mediante a ocorrencia 'n' da letra 'l'
        str,str,int->int"""
    i=0
    while i < len(texto):
        if letra in texto:
            frase=str.replace(texto,letra,'/',n-1)
        i=i+1

    if letra in frase:
        return frase.index(letra)
    else:
        return -1