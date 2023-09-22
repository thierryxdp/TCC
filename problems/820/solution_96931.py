def posLetra(frase,l,n):
    """Função que retorna a posição da string mediante a ocorrencia 'n' da letra 'l'
        str,str,int->int"""
    i=0
    while i < len(frase):
        if l in frase:
            frase=str.replace(frase,letra,'/',n-1)
        posicao=posicao+1

    if l in frase:
        return frase.index(l)
    else:
        return -1