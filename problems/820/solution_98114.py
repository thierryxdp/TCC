def posLetra(frase,letra,ocorrencia):
    """Função que procura a letra na ocorrencia dada caso possua ela retorna qual qual posição esta, se nao possui a ocorrencia procurada retorna -1.
    parametros: str,str,int->int"""
    posicao = frase.find(letra)
    while posicao >= 0 and ocorrencia > 1:
        posicao = frase.find(letra, posicao + 1)
        ocorrencia -= 1
    return posicao