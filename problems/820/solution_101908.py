def posLetra(frase,letra,ocorrencia):
    """Função que acha a letra desejada na ocorrência desejada na frase. Caso não haja, a função retorna -1"""
    """Parâmetros de entrada:str"""
    """Parâmetros de saída:str"""
    contador=0
    proximo=0
    while proximo<len(frase):
        if frase[proximo]==letra and contador==ocorrencia:
            contador+=1
        proximo+=1
        else:
            return -1
    return proximo