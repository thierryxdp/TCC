def posLetra(texto,letra,n):
    """Função que retorna a posição da string mediante a ocorrencia 'n' da letra 'l'
        str,str,int->int"""
    indice=0
    while indice < len(texto):
        if letra in texto:
            frase=str.replace(texto,letra,'/',n-1)
        posicao=posicao+1

    if letra in frase:
        return frase.index(let)
    else:
        return -1