def posLetra(frase,letra,ocorrencia):
    """Função que acha a letra desejada na ocorrência desejada na frase. Caso não haja, a função retorna -1"""
    """Parâmetros de entrada:str"""
    """Parâmetros de saída:str"""
    acumulador=0
    contador=0
    while contador<len(frase):
        if frase[contador]==letra:
            acumulador+=1
        elif frase[contador]==letra and acumulador==ocorrencia:
            return contador
        elif contador>len(frase) and acumulador==0:
            return -1
        contador+=1